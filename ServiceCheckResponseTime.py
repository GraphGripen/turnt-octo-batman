import os

import ServiceCheckConfig
import ServiceCheckFunction
import ServiceCheckClass

def getInformationDirectory(pathDir):
    detail = pathDir.split("\\")
    return detail
    
def infoServiceCheckResponseTime(type):
    infoResult = ServiceCheckClass.ServiceInfo()
    infoResult.creationTime = ServiceCheckFunction.getCurrentDateTime()
    if type == 101 : #case check interval(10Minute) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "10Minute"
    elif type == 102 : #case check interval(60Minute) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "60Minute"
    elif type == 103 : #case check interval(Daily) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "Daily"
    elif type == 104 : #case check interval(Minute) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "Minute"
    elif type == 105 : #case check interval(TAQCooked) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TAQCooked"
    elif type == 106 : #case check interval(TASCooked) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TASCooked"
    elif type == 107 : #case check interval(TASRAW) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TASRAW"
    elif type == 108 : #case check interval(TickTAQ) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TickTAQ"
    elif type == 109 : #case check interval(TickTAS) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TickTAS"
    elif type == 110 : #case check interval(Yearly) of type(RP)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "Yearly"
    elif type == 201 : #case check interval(10Minute) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "10Minute"
    elif type == 202 : #case check interval(60Minute) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "60Minute"
    elif type == 203 : #case check interval(Daily) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "Daily"
    elif type == 204 : #case check interval(Minute) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "Minute"
    elif type == 205 : #case check interval(TAQCooked) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TAQCooked"
    elif type == 206 : #case check interval(TASCooked) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TASCooked"
    elif type == 207 : #case check interval(TASRAW) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TASRAW"
    elif type == 208 : #case check interval(TickTAQ) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TickTAQ"
    elif type == 209 : #case check interval(TickTAS) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "TickTAS"
    elif type == 210 : #case check interval(Yearly) of type(Edge)
        infoResult.severity = ServiceCheckConfig.Developer['severity']
        infoResult.msg = "Yearly"
    
    return infoResult
     
     
def ServiceCheckResponseTime(path,responseTime):
    info = getInformationDirectory(path)
    type = info[len(info)-4]
    interval = info[len(info)-2]
    if ServiceCheckFunction.CheckResponseTime (type,interval,responseTime) == False :
        if type == "RP" :
            print "RUN 101\n"
            if interval == "10Minute" :
                info10Minute = infoServiceCheckResponseTime(101)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],info10Minute,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 102\n"
            elif interval == "60Minute" :
                info60Minute = infoServiceCheckResponseTime(102)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],info60Minute,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 103\n"
            elif interval == "Daily" :
                infoDaily = infoServiceCheckResponseTime(103)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoDaily,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 104\n"
            elif interval == "Minute" :
                infoMinute = infoServiceCheckResponseTime(104)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoMinute,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 105\n"
            elif interval == "TAQCooked" :
                infoTAQCooked = infoServiceCheckResponseTime(105)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTAQCooked,ServiceCheckConfig.Developer['splitSymbol'])    
            #print "RUN 106\n"
            elif interval == "TASCooked" :
                infoTASCooked = infoServiceCheckResponseTime(106)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTASCooked,ServiceCheckConfig.Developer['splitSymbol'])   
            #print "RUN 107\n"
            elif interval == "TASRAW" :
                infoTASRAW = infoServiceCheckResponseTime(107)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTASRAW,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 108\n"
            elif interval == "TickTAQ" :
                infoTickTAQ = infoServiceCheckResponseTime(108)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTickTAQ,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 109\n"
            elif interval == "TickTAS" :
                infoTickTAS = infoServiceCheckResponseTime(109)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTickTAS,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 110\n"
            elif interval == "Yearly" :
                infoYearly = infoServiceCheckResponseTime(110)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoYearly,ServiceCheckConfig.Developer['splitSymbol'])
        elif type == "Edge" :
            print "RUN 201\n"
            if interval == "10Minute" :
                info10Minute = infoServiceCheckResponseTime(201)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],info10Minute,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 202\n"
            elif interval == "60Minute" :
                info60Minute = infoServiceCheckResponseTime(202)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],info60Minute,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 203\n"
            elif interval == "Daily" :
                infoDaily = infoServiceCheckResponseTime(203)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoDaily,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 204\n"
            elif interval == "Minute" :
                infoMinute = infoServiceCheckResponseTime(204)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoMinute,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 205\n"
            elif interval == "TAQCooked" :
                infoTAQCooked = infoServiceCheckResponseTime(205)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTAQCooked,ServiceCheckConfig.Developer['splitSymbol'])    
            #print "RUN 206\n"
            elif interval == "TASCooked" :
                infoTASCooked = infoServiceCheckResponseTime(206)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTASCooked,ServiceCheckConfig.Developer['splitSymbol'])   
            #print "RUN 207\n"
            elif interval == "TASRAW" :
                infoTASRAW = infoServiceCheckResponseTime(207)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTASRAW,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 208\n"
            elif interval == "TickTAQ" :
                infoTickTAQ = infoServiceCheckResponseTime(208)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTickTAQ,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 209\n"
            elif interval == "TickTAS" :
                infoTickTAS = infoServiceCheckResponseTime(209)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoTickTAS,ServiceCheckConfig.Developer['splitSymbol'])
            #print "RUN 210\n"
            elif interval == "Yearly" :
                infoYearly = infoServiceCheckResponseTime(210)
                ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoYearly,ServiceCheckConfig.Developer['splitSymbol'])
            
            
if __name__ == '__main__':
    #print "111"
    #ServiceCheckResponseTime("D:\E2EPerformance\AppstatParser\logs\Edge\Default\10Minute\output_20150403_182511.csv",10)
    ServiceCheckResponseTime(r"C:\Users\U6031187\Desktop\Edge\Default\Daily\output_20150403_182511.csv",10)
