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
        sql = "INSERT INTO tour(TourID, UserID, TourCode, TourName, StartTime, TimeOfTour, IsSample, Status, IsPayment) VALUES(%s, %s, %s, %s, NOW(), %s, %s, %s, %s)"
        
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (refId, None, tourCode, tourName, timeOfTour, 1, 1, 0))
        self.conn.commit()
        

        collection = self.dbMongo["TourContractXML"]
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        contentXML = base64.b64encode(bytes(content, 'utf-8'))
        post = {"_id": str(uuid.uuid4()), "UserID": None, "TourID": refId, "CreatedTime": dt_string, "IsCreatedContract" : 0, "IsCancel": 0, "ContentDataXML": contentXML}
        collection.insert_one(post)

        pass
    
    # Lấy nội dung 
    def getContentXML(self, id):
        collection = self.dbMongo["TourContractXML"]
        data = collection.find_one({"TourID" : id})
        content = None
        if data is not None:
            content = data.get("ContentDataXML")
            content = base64.b64decode(data["ContentDataXML"]).decode("utf-8")
        return content 