import imp
from pickle import TRUE
from unicodedata import name
from unittest import result
from repository.destinationrepository import DestinationRepository
import json
import math

class DestinationService:
    dl = None
    def __init__(self) -> None:
        self.dl = DestinationRepository()

    def importProvince(self):
        self.dl.importProvince()
        pass

    def getAllProvince(self):
        return self.dl.getAllProvince()

    def getAllDistrict(self):
        return self.dl.getAllDistrict()

    def getProvinceByID(self, id):
        return self.dl.getProvinceByID(id)

    def getDistrictByID(self, id):
        return self.dl.getDistrictByID(id)

    def getDistrictInProvince(self, id):
        return self.dl.getDistrictInProvince(id)

    def updateDestination(self, data):
        dataMaster = data.get("data")
        listImage = data.get("image")
        action = data.get("action")
        ticketPrice = {}
        ticketPrice["Adult"] = int(dataMaster.get("adultPrice"))
        ticketPrice["Child"] = int(dataMaster.get("childPrice"))
        ticketPrice["Baby"] = int(dataMaster.get("babyPrice"))
        ticketPrice = json.dumps(ticketPrice)
        id = dataMaster.get("id")
        name = dataMaster.get("name")
        if(self.dl.checkDuplicate(id, name)):
            self.dl.updateData(dataMaster, listImage, ticketPrice, action)
            return True
        else:
            return False

    def getList(self, search, size, page):
        lstDes = self.dl.getList(search)
        totalPage = 0
        totalRecord = 0
        if len(lstDes) > 0:
            totalRecord = len(lstDes)
            totalPage = math.ceil(totalRecord / size)
            if page+1 == totalPage:
                lstDes = lstDes[page : ]
            else:
                lstDes = lstDes[page : page + size]
        listImage = []
        for des in lstDes:
            id = des["RefID"]
            lstImage = self.dl.getImageOfDestination(id)
            listImage.append({
                "ID" : id,
                "Image" : lstImage
            })

        result = {
            "data" : lstDes,
            "totalRecord" : totalRecord,
            "totalPage" : totalPage,
            "image" : listImage
        }

        return result

    def getDestinationByID(self, id):
        destination = self.dl.getDestinationByID(id)
        return destination

    def deleteDestination(self, id):
        destination = self.dl.getDestinationByID(id)
        if destination.get("data")[0].get("IsUsed") == 1:
            return False
        else:
            self.dl.deleteDestination(id)
            return True

    def deleteDestinationInProvince(self, id):
        return self.dl.getDestinationInProvince(id)