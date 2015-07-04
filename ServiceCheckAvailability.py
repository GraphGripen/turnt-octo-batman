import os

import ServiceCheckConfig
import ServiceCheckFunction
import ServiceCheckClass
       
def infoServiceCheckAvailability(type):
    infoResult = ServiceCheckClass.ServiceInfo()
    infoResult.creationTime = ServiceCheckFunction.getCurrentDateTime()
    if type == 101 : #case check AnalysisTestResult.py
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "File AnalysisTestResult.py is downed"
    elif type == 102 : #case check zipTSILog.py
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "File zipTSILog.py is downed"
    elif type == 103 : #case check HousekeepingLog.py
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "File HousekeepingLog.py is downed"
    elif type == 104 : #case check ContinuesRun_EikonMon.py
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "File ContinuesRun_EikonMon.py is downed"
    elif type == 105 : #case check EXEInTask (TsiLoadTest.exe)
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "File TsiLoadTest.exe is downed"
    elif type == 106 : #case check StatusService (Sensu Client Service)
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "Sensu-Client-Service is stopped"
    elif type == 107 : #case check SinceYaml (since-db1-e2e-perf.yaml)
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "File since-db1-e2e-perf.yaml is not changed"
    elif type == 108 : #case check SensuLog (sensu-client.log)
        infoResult.severity = ServiceCheckConfig.Operation['severity']
        infoResult.msg = "File sensu-client.log is not changed"
    
    return infoResult
  
def ServiceCheckAvailability():
    while(1):
        print "RUN 101\n"
        if ServiceCheckFunction.CheckRunningBAT("AnalysisTestResult",ServiceCheckConfig.pathCRBAT) == False :
            infoAnalysisTestResult = infoServiceCheckAvailability(101)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoAnalysisTestResult,ServiceCheckConfig.Operation['splitSymbol'])
        
        print "RUN 102\n"        
        if ServiceCheckFunction.CheckRunningBAT("zipTSILog",ServiceCheckConfig.pathCRBAT) == False  :
            infozipTSILog = infoServiceCheckAvailability(102)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infozipTSILog,ServiceCheckConfig.Operation['splitSymbol'])
        
        print "RUN 103\n"
        if ServiceCheckFunction.CheckRunningBAT("HousekeepingLog",ServiceCheckConfig.pathCRBAT) == False :
            infoHousekeepingLog = infoServiceCheckAvailability(103)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoHousekeepingLog,ServiceCheckConfig.Operation['splitSymbol'])
        
        print "RUN 104\n"
        if ServiceCheckFunction.CheckRunningBAT("ContinuesRun_EikonMon",ServiceCheckConfig.pathCRBAT) == False :
            infoEikonMon = infoServiceCheckAvailability(104)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEikonMon,ServiceCheckConfig.Operation['splitSymbol'])
        
        print "RUN 105\n"
        if ServiceCheckFunction.CheckEXEInTask(ServiceCheckConfig.FileTsiLoadTest,ServiceCheckConfig.waitTimeCEXEIT) == False :
            infoEXEInTask = infoServiceCheckAvailability(105)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEXEInTask,ServiceCheckConfig.Operation['splitSymbol'])
        
        print "RUN 106\n"
        if ServiceCheckFunction.CheckStatusService (ServiceCheckConfig.nameService) == False :
            infoStatusService = infoServiceCheckAvailability(106)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoStatusService,ServiceCheckConfig.Operation['splitSymbol'])
        
        print "RUN 107\n"        
        if ServiceCheckFunction.CheckSinceYaml (ServiceCheckConfig.pathCSY,ServiceCheckConfig.waitTimeCSY) == False :
            infoSinceYaml = infoServiceCheckAvailability(107)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSinceYaml,ServiceCheckConfig.Operation['splitSymbol'])
        
        print "RUN 108\n"        
        if ServiceCheckFunction.CheckSensuLog (ServiceCheckConfig.pathCSL,ServiceCheckConfig.waitTimeCSL) == False :
            infoSensuLog = infoServiceCheckAvailability(108)
            ServiceCheckFunction.generateReportLog(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSensuLog,ServiceCheckConfig.Operation['splitSymbol'])

        
if __name__ == '__main__':
    ServiceCheckAvailability()
