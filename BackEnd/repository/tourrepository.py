from unittest import result
from torch import t
from .dlbase import DLBase
import xml.etree.ElementTree as et
import uuid
import base64
from datetime import datetime

class TourRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getCompanyInfo(self):
        sql = "Select * from company"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall()
        records[0].pop("CompanyID", None)
        return records[0]

    def getDefaultTourXML(self):
        tree = et.parse("./repository/Template/ContentContract.xml")
        return tree

    def getDefaultTourContract(self):
        pass
    
    # Tạo tour du lịch
    def CreateTour(self, data, content):
        refId = str(uuid.uuid4())
        tourName = data["Master"].get("TourName")
        timeOfTour = int(data["Contract"].get("TotalHour"))
        tourCode = data["Master"].get("ContractCode")
        userID = data["Info"].get("UserID")
        sample = int(data["Info"].get("Sample"))
        status = int(data["Info"].get("Status"))
        isPayment = int(data["Info"].get("IsPayment"))
        sql = "INSERT INTO tour(TourID, UserID, TourCode, TourName, StartTime, TimeOfTour, IsSample, Status, IsPayment) VALUES(%s, %s, %s, %s, NOW(), %s, %s, %s, %s)"
        
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (refId, userID, tourCode, tourName, timeOfTour, sample, status, isPayment))
        self.conn.commit()
        

        collection = self.dbMongo["TourContractXML"]
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        contentXML = base64.b64encode(bytes(content, 'utf-8'))
        post = {"_id": str(uuid.uuid4()), "UserID": userID, "TourID": refId, "CreatedTime": dt_string, "IsCreatedContract" : 0, "IsCancel": status, "ContentDataXML": contentXML}
        collection.insert_one(post)

        pass

    def UpdateTour(self, data, content):
        refId = data["Info"].get("RefID")
        tourName = data["Master"].get("TourName")
        timeOfTour = int(data["Contract"].get("TotalHour"))
        tourCode = data["Master"].get("ContractCode")
        userID = data["Info"].get("UserID")
        sample = int(data["Info"].get("Sample"))
        status = int(data["Info"].get("Status"))
        isPayment = int(data["Info"].get("IsPayment"))
        sql = "UPDATE tour SET TourName = %s ,TimeOfTour = %s ,Status = %s ,IsPayment = %s WHERE TourID = %s;"
        
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (tourName, timeOfTour, status, isPayment, refId))
        self.conn.commit()
        
        contentXML = base64.b64encode(bytes(content, 'utf-8'))
        collection = self.dbMongo["TourContractXML"]
        myquery = { "TourID": refId }
        newvalues = { "$set": { "ContentDataXML": contentXML, "IsCancel" : status } }

        collection.update_one(myquery, newvalues)

    def checkDuplicate(self, data):
        refId = data["Info"].get("RefID")
        tourName = data["Master"].get("TourName")

        sql = "SELECT * FROM tour t WHERE t.RefID <> %s AND LOWER(t.TourName) = %s"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (refId, tourName.lower()))
        records = cursor.fetchall()
        if len(records) > 0:
            return False
        else:
            return True
    
    # Lấy nội dung 
    def getContentXML(self, id):
        collection = self.dbMongo["TourContractXML"]
        data = collection.find_one({"TourID" : id})
        content = None
        if data is not None:
            content = data.get("ContentDataXML")
            content = base64.b64decode(data["ContentDataXML"]).decode("utf-8")
        return content 

    def getLastTourCode(self):
        sql = "SELECT MAX(CAST(SUBSTRING(t.TourCode, 2, LENGTH(t.TourCode)) AS SIGNED)) AS LASTCODE FROM tour t;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall()
        return records[0]

    def getList(self, search, isStop, mode):
        cursor = self.conn.cursor(dictionary=True)
        # mode = 1: tour mau. mode = 2: tour cho xac nhan. mode = 3: tour da tao contract
        if mode == 1:
            if search != None and search != "":
                if isStop == 1:
                    sql = "SELECT * FROM tour t WHERE t.IsSample = 1 AND (MATCH(t.TourName) AGAINST (%s) OR t.TourCode = %s) AND t.Status = 1 ORDER BY t.TourCode DESC"
                    cursor.execute(sql, (search,search))
                else:
                    sql = "SELECT * FROM tour t WHERE t.IsSample = 1 AND (MATCH(t.TourName) AGAINST (%s) OR t.TourCode = %s) ORDER BY t.TourCode DESC"
                    cursor.execute(sql, (search,search))
                records = cursor.fetchall()
                return records
            else:
                if isStop == 1:
                    sql = "SELECT * FROM tour t WHERE t.IsSample = 1 AND t.Status = 1 ORDER BY t.TourCode DESC" 
                    cursor.execute(sql)
                else:
                    sql = "SELECT * FROM tour t WHERE t.IsSample = 1 ORDER BY t.TourCode DESC"
                    cursor.execute(sql)
                records = cursor.fetchall()
                return records
        elif mode == 2:
            if search != None and search != "":
                sql = "SELECT t.*, u.Name AS UserName FROM tour t, user u WHERE t.UserID = u.UserID AND t.IsSample = 0 AND (MATCH(t.TourName) AGAINST (%s) OR t.TourCode = %s) ORDER BY t.TourCode DESC"
                cursor.execute(sql, (search,search))
            else:
                sql = "SELECT t.*, u.Name AS UserName FROM tour t, user u WHERE t.UserID = u.UserID AND t.IsSample = 0 ORDER BY t.TourCode DESC"
                cursor.execute(sql, (search,search))
    
            records = cursor.fetchall()
            result = records
            listRefID = []
            for record in records:
                listRefID.append(record["TourID"])

            collection = self.dbMongo["TourContractXML"]
            tour = collection.find({"TourID" : { "$in" : listRefID }, "IsCreatedContract" : 0})
            lstTourID = []
            for t in tour:
                lstTourID.append(t["TourID"])
            
            result = list(filter(lambda x: x["TourID"] in lstTourID, result))
            return result

        else:
            if search != None and search != "":
                sql = "SELECT t.*, u.Name AS UserName FROM tour t, user u WHERE t.UserID = u.UserID AND t.IsSample = 0 AND (MATCH(t.TourName) AGAINST (%s) OR t.TourCode = %s) ORDER BY t.TourCode DESC"
                cursor.execute(sql, (search,search))
            else:
                sql = "SELECT t.*, u.Name AS UserName FROM tour t, user u WHERE t.UserID = u.UserID AND t.IsSample = 0 ORDER BY t.TourCode DESC"
                cursor.execute(sql, (search,search))
    
            records = cursor.fetchall()
            result = records
            listRefID = []
            for record in records:
                listRefID.append(record["TourID"])

            collection = self.dbMongo["TourContractXML"]
            tour = collection.find({"TourID" : { "$in" : listRefID }, "IsCreatedContract" : 1})
            lstTourID = []
            for t in tour:
                lstTourID.append(t["TourID"])
            
            result = list(filter(lambda x: x["TourID"] in lstTourID, result))
            return result

    def deleteTemplate(self, id):
        sql = "DELETE FROM tour WHERE TourID = %s"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        self.conn.commit()
        collection = self.dbMongo["TourContractXML"]
        myquery = { "TourID": id }
        collection.delete_one(myquery)

    def updateStatusTemplate(self, id, status):
        sql = "UPDATE tour SET Status = %s WHERE TourID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (status, id))
        self.conn.commit()

    def getByID(self, id):
        sql = "SELECT *  FROM tour t WHERE t.TourID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id, ))
        records = cursor.fetchall()
        return records[0]