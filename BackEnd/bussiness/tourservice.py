from cmath import atan, cos
from traceback import print_tb
from repository.tourrepository import TourRepository
import xml.etree.ElementTree as et
from datetime import datetime
import lxml.html
from lxml import etree
import math
from datetime import datetime

class TourService:
    dl = None
    def __init__(self) -> None:
        self.dl = TourRepository()

    def updateTour(self, data):
        if(self.checkDuplicate):
            content = self.createDataXML(data)
            if int(data["Info"].get("Mode")) == 1:
                self.dl.CreateTour(data, content)
            else:
                self.dl.UpdateTour(data, content)
            return True
        else:
            return False

    def checkDuplicate(self, data):
        return self.dl.checkDuplicate()

    def createDataXML(self, data):
        doc = self.dl.getDefaultTourXML()
        root = doc.getroot()
        contentMaster = data["Master"]
        contractInfo = data["Contract"]
        destination = data["Destination"]
        schedule = data["Schedule"]
        customerRequest = data["CustomerRequest"]
        attachOption = data["AttachOption"]
        refundPolicy = data["RefundPolicy"]
        tutorial = data["Tutorial"]
        companyInfo = self.dl.getCompanyInfo()

        root = self.bindingContractMaster(contentMaster, root)
        root = self.bindingContractInfo(contractInfo, root)
        root = self.bindingContractMaster(companyInfo, root)
        root = self.bindingContractDestination(destination, root)
        root = self.bindingSchedule(schedule, root)
        root = self.bindingCustomerRequest(customerRequest, root)
        root = self.bindingAttachOption(attachOption, root)
        root = self.bindingRefundPolicy(refundPolicy, root)
        root = self.bindingTutorial(tutorial, root)

        content = et.tostring(root, encoding='unicode', method='xml')
        return content


    # Bind thông tin chung của hợp đồng
    def bindingContractMaster(self, data, root):
        for key, value in data.items():
            node = root.find("" + str(key))
            if node is not None:
                node.text = str(value)
        return root

    # Bind thông tin về số lượng của hợp đồng
    def bindingContractInfo(self, data, root):
        for key, value in data.items():
            node = root.find("ContractInfo/" + str(key))
            if node is not None:
                node.text = str(value)
        return root

    # Bind danh sách điểm đến
    def bindingContractDestination(self, data, root):
        destination = root.find("./ContractData/DestinationItem")
        for des in destination.findall("Destination"):
            destination.remove(des)

        for item in data:
            des = et.Element("Destination")
            destination.append(des)

            name = et.SubElement(des, "Name")
            name.text = item["Name"]
            address = et.SubElement(des, "Address")
            address.text = item["Address"]
            
            ticketPrice = et.SubElement(des, "TicketPrice")
            adultPrice = et.SubElement(ticketPrice, "Adult")
            adultPrice.text = str(item["TicketPrice"].get("Adult"))
            childPrice = et.SubElement(ticketPrice, "Child")
            childPrice.text = str(item["TicketPrice"].get("Child"))
            babyPrice = et.SubElement(ticketPrice, "Baby")
            babyPrice.text = str(item["TicketPrice"].get("Baby"))

            destinationID = et.SubElement(des, "DestinationID")
            destinationID.text = item["DestinationID"]
        
        return root

    # Bind lịch trình
    def bindingSchedule(self, data, root):
        schedule = root.find("./ContractData/Schedule")
        for sche in schedule.findall("Day"):
            schedule.remove(sche)

        for i in range(len(data)):
            item = data[i]
            day = et.Element("Day")
            schedule.append(day)
            order = et.SubElement(day, "SortOrder")
            order.text = str(i + 1)

            lstMorning = item.get("Morning")
            lstAfternoon = item.get("Afternoon")
            lstEvening = item.get("Evening")
            moring = et.SubElement(day, "Morning")
            afternoon = et.SubElement(day, "Afternoon")
            evening = et.SubElement(day, "Evening")

            # Hoạt động buổi sáng
            for act in lstMorning:
                active = et.Element("Activity")
                moring.append(active)
                startTime = et.SubElement(active, "StartTime")
                place = et.SubElement(active, "Destination")
                action = et.SubElement(active, "Action")
                destinationID = et.SubElement(active, "DestinationID")

                startTime.text = act["StartTime"]
                place.text = act["Destination"]
                action.text = act["Action"]
                destinationID.text = act["DestinationID"]

            # Hoạt động buổi chiều
            for act in lstAfternoon:
                active = et.Element("Activity")
                afternoon.append(active)
                startTime = et.SubElement(active, "StartTime")
                place = et.SubElement(active, "Destination")
                action = et.SubElement(active, "Action")
                destinationID = et.SubElement(active, "DestinationID")

                startTime.text = act["StartTime"]
                place.text = act["Destination"]
                action.text = act["Action"]
                destinationID.text = act["DestinationID"]

            
            # Hoạt động buổi tối
            for act in lstEvening:
                active = et.Element("Activity")
                evening.append(active)
                startTime = et.SubElement(active, "StartTime")
                place = et.SubElement(active, "Destination")
                action = et.SubElement(active, "Action")
                destinationID = et.SubElement(active, "DestinationID")

                startTime.text = act["StartTime"]
                place.text = act["Destination"]
                action.text = act["Action"]
                destinationID.text = act["DestinationID"]

        return root   

    # Bind yêu cầu của KH
    def bindingCustomerRequest(self, data, root):
        request = root.find("./ContractData/CustomerRequest")
        for res in request.findall("Item"):
            request.remove(res)

        for i in range(len(data)):
            item = data[i]
            res = et.Element("Item")
            request.append(res)
            order = et.SubElement(res, "SortOrder")
            order.text = str(i + 1)
            content = et.SubElement(res, "Content")
            content.text = item["Content"]
        
        return root

    # Bind chi phí đi kèm
    def bindingAttachOption(self, data, root):
        option = root.find("./ContractData/AttachOption")
        for op in option.findall("Item"):
            option.remove(op)

        for i in range(len(data)):
            item = data[i]
            op = et.Element("Item")
            option.append(op)
            order = et.SubElement(op, "SortOrder")
            order.text = str(i + 1)
            content = et.SubElement(op, "Content")
            content.text = item["Content"]
            cost = et.SubElement(op, "Cost")
            cost.text = str(item["Cost"])
        
        return root

    # Bind chính sách hoàn hủy
    def bindingRefundPolicy(self, data, root):
        policy = root.find("./ContractData/RefundPolicy")
        for po in policy.findall("Item"):
            policy.remove(po)

        for i in range(len(data)):
            item = data[i]
            po = et.Element("Item")
            policy.append(po)
            order = et.SubElement(po, "SortOrder")
            order.text = str(i + 1)
            content = et.SubElement(po, "Content")
            content.text = item["Content"]
        
        return root

    # Bind thông tin hướng dẫn
    def bindingTutorial(self, data, root):
        tutorial = root.find("./ContractData/Tutorial")
        for tuto in tutorial.findall("Item"):
            tutorial.remove(tuto)

        for i in range(len(data)):
            item = data[i]
            tuto = et.Element("Item")
            tutorial.append(tuto)
            order = et.SubElement(tuto, "SortOrder")
            order.text = str(i + 1)
            content = et.SubElement(tuto, "Content")
            content.text = item["Content"]
        
        return root

    # Lấy nội dung html của tour
    def getTourHTML(self, id):
        xslt_doc = etree.parse("./repository/Template/template_tour_contract.xslt")
        xslt_transformer = etree.XSLT(xslt_doc)
        xml = self.dl.getContentXML(id)
        if xml is not None:
            source_doc = etree.fromstring(xml)
            output_doc = xslt_transformer(source_doc)
            html = str(output_doc)
            return html
        else:
            return "<html></html>"

    def getNewTourCode(self):
        lastCode = self.dl.getLastTourCode()
        newCode = ""
        if lastCode["LASTCODE"] == None:
            newCode = "T0001"
        else:
            newIndex = str(lastCode["LASTCODE"] + 1)
            while len(newIndex) < 4:
                newIndex = "0" + newIndex
            newCode = "T" + newIndex
        return newCode

    def getList(self, search, size, page, isStop, mode):
        lstTour = self.dl.getList(search, isStop, mode)
        totalPage = 0
        totalRecord = 0
        if len(lstTour) > 0:
            totalRecord = len(lstTour)
            totalPage = math.ceil(totalRecord / size)
            if page+1 == totalPage:
                lstTour = lstTour[page : ]
            else:
                lstTour = lstTour[page : page + size]
        
        for item in lstTour:
            item["StartTime"] = item["StartTime"].strftime("%d/%m/%Y")
            if item["Status"] == 1:
                item["Status"] = "Đang sử dụng"
            else:
                item["Status"] = "Ngừng sử dụng"
        result = {
            "data" : lstTour,
            "totalRecord" : totalRecord,
            "totalPage" : totalPage
        }

        return result
            
    def deleteTemplate(self, id):
        self.dl.deleteTemplate(id)

    def updateStatusTemplate(self, id, status):
        self.dl.updateStatusTemplate(id, status)

    def getByID(self, id):
        xml = self.dl.getContentXML(id)
        # doc = et.parse(xml)
        root = et.fromstring(xml)

        data = {"Master" : {}, "Contract" : {}, "Destination": [], "Schedule": [], "CustomerRequest" : [], "AttachOption" : [], "RefundPolicy" : [], "Tutorial": [], "Info": {}}

        data["Master"]["ContractCode"] = root.find("ContractCode").text
        data["Master"]["CreatedTime"] = root.find("CreatedTime").text
        data["Master"]["TotalCost"] = root.find("TotalCost").text
        data["Master"]["TourName"] = root.find("TourName").text
        data["Master"]["ProvinceStartID"] = root.find("ProvinceStartID").text
        data["Master"]["ProvinceStartName"] = root.find("ProvinceStartName").text
        data["Master"]["ProvinceDestinationID"] = root.find("ProvinceDestinationID").text
        data["Master"]["ProvinceDestinationName"] = root.find("ProvinceDestinationName").text
        data["Master"]["PickupAdress"] = root.find("PickupAdress").text
        data["Master"]["PickupTime"] = root.find("PickupTime").text

        data["Contract"]["NumberAdult"] = root.find("ContractInfo/NumberAdult").text
        data["Contract"]["NumberChild"] = root.find("ContractInfo/NumberChild").text
        data["Contract"]["NumberBaby"] = root.find("ContractInfo/NumberBaby").text
        data["Contract"]["StartTime"] = root.find("ContractInfo/StartTime").text
        data["Contract"]["EndTime"] = root.find("ContractInfo/EndTime").text
        data["Contract"]["TotalHour"] = root.find("ContractInfo/TotalHour").text

        destination = root.find("./ContractData/DestinationItem")
        for des in destination.findall("Destination"):
            data["Destination"].append({
                "Name" : des.find("Name").text,
                "Address" : des.find("Address").text,
                "TicketPrice" : {
                    "Adult" : des.find("TicketPrice/Adult").text,
                    "Child" : des.find("TicketPrice/Child").text,
                    "Baby" : des.find("TicketPrice/Baby").text,
                },
                "RefID" : des.find("DestinationID").text
            })

        schedule = root.find("./ContractData/Schedule")
        day = schedule.findall("Day")
        for i in range(len(day)):
            sche = day[i]
            data["Schedule"].append({
                "Morning" : [],
                "Afternoon" : [],
                "Evening" : []
            })

            moring = sche.find("Morning").findall("Activity")
            for act in moring:
                data["Schedule"][i].get("Morning").append({
                    "RefID": act.find("DestinationID").text,
                    "Name": act.find("Destination").text,
                    "Time": act.find("StartTime").text,
                    "Action": act.find("Action").text,
                })

            afternoon = sche.find("Afternoon").findall("Activity")
            for act in afternoon:
                data["Schedule"][i].get("Afternoon").append({
                    "RefID": act.find("DestinationID").text,
                    "Name": act.find("Destination").text,
                    "Time": act.find("StartTime").text,
                    "Action": act.find("Action").text,
                })
            
            evening = sche.find("Evening").findall("Activity")
            for act in evening:
                data["Schedule"][i].get("Evening").append({
                    "RefID": act.find("DestinationID").text,
                    "Name": act.find("Destination").text,
                    "Time": act.find("StartTime").text,
                    "Action": act.find("Action").text,
                })

        request = root.find("./ContractData/CustomerRequest")
        for req in request.findall("Item"):
            data["CustomerRequest"].append({
                "Content" : req.find("Content").text
            })

        option = root.find("./ContractData/AttachOption")
        for op in option.findall("Item"):
            data["AttachOption"].append({
                "Name" : op.find("Content").text,
                "Price" : op.find("Cost").text
            })

        policy = root.find("./ContractData/RefundPolicy")
        for po in policy.findall("Item"):
            data["RefundPolicy"].append({
                "Content" : po.find("Content").text
            })

        tutorial = root.find("./ContractData/Tutorial")
        for tu in tutorial.findall("Item"):
            data["Tutorial"].append({
                "Content" : tu.find("Content").text
            })

        dataSQL = self.dl.getByID(id)
        data["Info"]["RefID"] = dataSQL["TourID"]
        data["Info"]["Sample"] = dataSQL["IsSample"]
        data["Info"]["Status"] = dataSQL["Status"]
        data["Info"]["IsPayment"] = dataSQL["IsPayment"]

        return data
