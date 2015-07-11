import os

import ServiceCheckConfig
import ServiceCheckFunction
import ServiceCheckClass

def getInformationDirectory(pathDir):
    detail = pathDir.split("\\")
    return detail
    
def infoServiceCheckResponseTime(type,interval,responseTime):
    infoResult = ServiceCheckClass.ServiceInfo()
    infoResult.creationTime = ServiceCheckFunction.getCurrentDateTime_version1()
    infoResult.severity = ServiceCheckConfig.Developer['severity']
    infoResult.msg = "Detect spike " + str(responseTime) + " ms in " + interval.lower() + " of " + type.lower()
    
    return infoResult
     
def ServiceCheckResponseTime(path,responseTime):
    info = getInformationDirectory(path)
    type = info[len(info)-4]
    interval = info[len(info)-2]
    if ServiceCheckFunction.CheckResponseTime (type,interval,responseTime) == False :
        infoDetect = infoServiceCheckResponseTime(type,interval,responseTime)
        ServiceCheckFunction.generateReportLog_version1(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoDetect,ServiceCheckConfig.Developer['splitSymbol'])
            
            
if __name__ == '__main__':
    print "Reuters"
    #Function ServiceCheckResponseTime Parameter1 = path of file.csv /// Parameter2 = Response Times
    #For Example, ServiceCheckResponseTime("D:\E2EPerformance\AppstatParser\logs\Edge\Default\10Minute\output_20150403_182511.csv",10)
    ServiceCheckResponseTime(r"C:\Users\U6031187\Desktop\Edge\Default\Daily\output_20150403_182511.csv",10)
