from cmath import cos
from traceback import print_tb
from repository.tourrepository import TourRepository
import xml.etree.ElementTree as et
from datetime import datetime
import lxml.html
from lxml import etree

class TourService:
    dl = None
    def __init__(self) -> None:
        self.dl = TourRepository()

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
        self.dl.CreateTour(data, content)


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
            adultPrice.text = str(item["Adult"])
            childPrice = et.SubElement(ticketPrice, "Child")
            childPrice.text = str(item["Child"])
            babyPrice = et.SubElement(ticketPrice, "Baby")
            babyPrice.text = str(item["Baby"])

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

            lstMorning = item["Morning"]
            lstAfternoon = item["Afternoon"]
            lstEvening = item["Evening"]
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

                startTime.text = act["StartTime"]
                place.text = act["Destination"]
                action.text = act["Action"]

            # Hoạt động buổi chiều
            for act in lstAfternoon:
                active = et.Element("Activity")
                afternoon.append(active)
                startTime = et.SubElement(active, "StartTime")
                place = et.SubElement(active, "Destination")
                action = et.SubElement(active, "Action")

                startTime.text = act["StartTime"]
                place.text = act["Destination"]
                action.text = act["Action"]

            
            # Hoạt động buổi tối
            for act in lstEvening:
                active = et.Element("Activity")
                evening.append(active)
                startTime = et.SubElement(active, "StartTime")
                place = et.SubElement(active, "Destination")
                action = et.SubElement(active, "Action")

                startTime.text = act["StartTime"]
                place.text = act["Destination"]
                action.text = act["Action"]

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
            return str(output_doc)
        else:
            return None
            

