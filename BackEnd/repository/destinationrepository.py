from .dlbase import DLBase
import json
import uuid
import base64

class DestinationRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def importProvince(self):
        f_listProvince = open("./repository/Template/province.json", "r", encoding="utf-8-sig")
        province = json.load(f_listProvince)
        f_listProvince.close()

        sqlProvince = "INSERT INTO province(ProvinceID, ProvinceName) VALUES (%s, %s)"
        sqlDistrict = "INSERT INTO district(DistrictID, ProvinceID, DistrictName) VALUES (%s, %s, %s)"
        recordInsertProvince = []
        recordInsertDistrict = []

        for p in province:
            refID = str(uuid.uuid4())
            provinceName = p["name"]
            recordInsertProvince.append((refID, provinceName))
            for d in p["districts"]:
                id = str(uuid.uuid4())
                name = d["name"]
                recordInsertDistrict.append((id, refID, name))

        cursor = self.conn.cursor(dictionary=True)
        cursor.executemany(sqlProvince, recordInsertProvince)
        self.conn.commit()
        
        cursor = self.conn.cursor(dictionary=True)
        cursor.executemany(sqlDistrict, recordInsertDistrict)
        self.conn.commit()

        cursor.close()
    
    def getAllProvince(self):
        sql = "SELECT * FROM province"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall()
        return records

    def getProvinceByID(self, id):
        sql = "SELECT * FROM province p WHERE p.ProvinceID = %s" 
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        return records

    def getAllDistrict(self):
        sql = "SELECT * FROM district"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall()
        return records

    def getDistrictByID(self, id):
        sql = "SELECT * FROM district d WHERE d.DistrictID = %s" 
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        return records

    def getDistrictInProvince(self, pID):
        sql = "SELECT * FROM district d WHERE d.ProvinceID = %s" 
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (pID,))
        records = cursor.fetchall()
        return records

    def checkDuplicate(self, id, name):
        sql = "SELECT * FROM tourdestination t WHERE t.RefID <> %s AND LOWER(t.Name) = %s"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id, name.lower()))
        records = cursor.fetchall()
        if len(records) > 0:
            return False
        else:
            return True

    def updateData(self, data, image, ticketPrice, action):
        sql = ""
        if action == 0:
            sql = "INSERT INTO tourdestination(RefID,ProvinceID,DistrictID,Name,Place,Described,TicketPrice,IsUsed,ProvinceName,DistrictName)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        else:
            sql = "UPDATE tourdestination SET ProvinceID = %s, DistrictID = %s, Name = %s, Place = %s, Described = %s, TicketPrice = %s, IsUsed = %s, ProvinceName = %s, DistrictName = %s WHERE RefID = %s"
        
        cursor = self.conn.cursor(dictionary=True)
        if action == 0:
            cursor.execute(sql, (data.get("id"), data.get("provinceID"), data.get("districtID"), data.get("name"), data.get("address"), data.get("describled"), ticketPrice, data.get("used"), data.get("pronvinceName"), data.get("districtName")))
        else:
            cursor.execute(sql, (data.get("provinceID"), data.get("districtID"), data.get("name"), data.get("address"), data.get("describled"), ticketPrice, data.get("used"), data.get("pronvinceName"), data.get("districtName"), data.get("id")))
        self.conn.commit()

        collection = self.dbMongo["TourDestinationImage"]
        myquery = { "TourDestinationID": data.get("id") }
        collection.delete_many(myquery)

        listImage = []
        for item in image:
            dic = {"_id": str(uuid.uuid4()), "TourDestinationID": data.get("id"), "ContentImage": item}
            listImage.append(dic)

        collection.insert_many(listImage)

    def getList(self, search):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM tourdestination t WHERE MATCH(t.Name) AGAINST (%s) OR MATCH(t.Place) AGAINST (%s)"
        if search == None or search == "":
            sql = "SELECT * FROM tourdestination"
            cursor.execute(sql)
            records = cursor.fetchall()
            return records
        else:  
            cursor.execute(sql, (search, search))
            records = cursor.fetchall()
            return records

    def getDestinationByID(self, id):
        sql = "SELECT * FROM tourdestination t WHERE t.RefID = %s"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        records = cursor.fetchall()

        collection = self.dbMongo["TourDestinationImage"]
        image = collection.find({"TourDestinationID" : id})
        lstImgae = []
        for item in image:
            lstImgae.append(item.get("ContentImage"))

        result = {
            "data" : records,
            "image" : lstImgae
        }

        return result

    

    def deleteDestination(self, id):
        sql = "DELETE FROM tourdestination WHERE RefID = %s"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        self.conn.commit()
        collection = self.dbMongo["TourDestinationImage"]
        myquery = { "TourDestinationID": id }
        collection.delete_many(myquery)

    def getDestinationInProvince(self, id):
        sql = "SELECT t.RefID, t.Name, t.Place, t.TicketPrice FROM tourdestination t WHERE t.ProvinceID = %s"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        return records

    def getImageOfDestination(self, id):
        collection = self.dbMongo["TourDestinationImage"]
        image = collection.find({"TourDestinationID" : id})
        lstImgae = []
        for item in image:
            lstImgae.append(item.get("ContentImage"))

        return lstImgae

    def getImageOfDestinations(self, lstID):
        collection = self.dbMongo["TourDestinationImage"]
        image = collection.find({"TourDestinationID" : { "$in" : lstID }})
        lstImgae = []
        for item in image:
            lstImgae.append(item.get("ContentImage"))
        return lstImgae