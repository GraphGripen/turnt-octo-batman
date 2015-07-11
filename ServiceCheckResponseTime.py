import os

import ServiceCheckConfig
import ServiceCheckFunction
import ServiceCheckClass
   
def infoServiceCheckResponseTime(server,type,interval,responseTime):
    infoResult = ServiceCheckClass.ServiceInfo()
    infoResult.creationTime = ServiceCheckFunction.getCurrentDateTime_version1()
    infoResult.severity = ServiceCheckConfig.Developer['severity']
    infoResult.msg = "Detect spike " + str(responseTime) + " ms in " + interval + " of " + type + " at " + server
    
    return infoResult
     
def ServiceCheckResponseTime(testCase,responseTime):
    info = testCase.split("-") #Format Example => TASCooked-STC-Edge-Default-1
    server = info[1]
    type = info[2]
    interval = info[0]
    if ServiceCheckFunction.CheckResponseTime (server,type,interval,responseTime) == False :
        infoDetect = infoServiceCheckResponseTime(server,type,interval,responseTime)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathDeveloper,ServiceCheckConfig.Developer['logname'],infoDetect,ServiceCheckConfig.Developer['splitSymbol'])
            
            
if __name__ == '__main__':
    print "Reuters"
    #Function ServiceCheckResponseTime Parameter1 = Test case (collumn2 in file.csv) /// Parameter2 = Response Times (collumn4 in file.csv)
    #For Example, ServiceCheckResponseTime("TASCooked-STC-Edge-Default-1",10)
    ServiceCheckResponseTime("TASCooked-STC-Edge-Default-1",10)
