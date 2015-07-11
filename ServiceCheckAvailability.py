import os
import thread
import time

import ServiceCheckConfig
import ServiceCheckFunction
import ServiceCheckClass
import ServiceCheckRecovery
       
def infoServiceCheckAvailability(severity,msg):
    infoResult = ServiceCheckClass.ServiceInfo()
    infoResult.creationTime = ServiceCheckFunction.getCurrentDateTime_version2()
    infoResult.severity = severity
    infoResult.msg = msg
    
    return infoResult
    
def runServiceCheckAvailability_101():
    print "RUN Check AnalysisTestResult.py\n"
    if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile1'],ServiceCheckConfig.pathCRBAT) == False :
        #Notify ==> AnalysisTestResult.py isn't running
        infoAnalysisTestResult = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_101)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoAnalysisTestResult,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> AnalysisTestResult.py is start recoverring
        infoAnalysisTestResult = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_101['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoAnalysisTestResult,ServiceCheckConfig.Operation['splitSymbol'])
            
        if ServiceCheckRecovery.RecoveryRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile1']) == True :
            if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile1'],ServiceCheckConfig.pathCRBAT) == True :
                #Notify ==> AnalysisTestResult.py recoverred successful
                infoAnalysisTestResult = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_101['complete'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoAnalysisTestResult,ServiceCheckConfig.Operation['splitSymbol'])
            else :
                #Notify ==> AnalysisTestResult.py recoverred not successful
                infoAnalysisTestResult = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_101['fail'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoAnalysisTestResult,ServiceCheckConfig.Operation['splitSymbol'])
        else :
            #Notify ==> AnalysisTestResult.py recoverred not successful
            infoAnalysisTestResult = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_101['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoAnalysisTestResult,ServiceCheckConfig.Operation['splitSymbol'])
    
def runServiceCheckAvailability_102():
    print "RUN Check zipTSILog.py\n"        
    if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile2'],ServiceCheckConfig.pathCRBAT) == False  :
        #Notify ==> zipTSILog.py isn't running
        infozipTSILog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_102)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infozipTSILog,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> zipTSILog.py is start recoverring
        infozipTSILog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_102['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infozipTSILog,ServiceCheckConfig.Operation['splitSymbol'])
            
        if ServiceCheckRecovery.RecoveryRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile2']) == True :  
            if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile2'],ServiceCheckConfig.pathCRBAT) == True :
                #Notify ==> zipTSILog.py recoverred successful
                infozipTSILog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_102['complete'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infozipTSILog,ServiceCheckConfig.Operation['splitSymbol'])
            else :
                #Notify ==> zipTSILog.py recoverred not successful
                infozipTSILog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_102['fail'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infozipTSILog,ServiceCheckConfig.Operation['splitSymbol'])
        else:
            #Notify ==> zipTSILog.py recoverred not successful
            infozipTSILog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_102['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infozipTSILog,ServiceCheckConfig.Operation['splitSymbol'])

def runServiceCheckAvailability_103():
    print "RUN Check HousekeepingLog.py\n"
    if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile3'],ServiceCheckConfig.pathCRBAT) == False :
        #Notify ==> HousekeepingLog.py isn't running
        infoHousekeepingLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_103)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoHousekeepingLog,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> HousekeepingLog.py is start recoverring
        infoHousekeepingLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_103['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoHousekeepingLog,ServiceCheckConfig.Operation['splitSymbol'])
            
        if ServiceCheckRecovery.RecoveryRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile3']) == True :
            if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile3'],ServiceCheckConfig.pathCRBAT) == True :
                #Notify ==> HousekeepingLog.py recoverred successful
                infoHousekeepingLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_103['complete'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoHousekeepingLog,ServiceCheckConfig.Operation['splitSymbol'])
            else :
                #Notify ==> HousekeepingLog.py recoverred not successful
                infoHousekeepingLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_103['fail'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoHousekeepingLog,ServiceCheckConfig.Operation['splitSymbol'])
        else:
            #Notify ==> HousekeepingLog.py recoverred not successful
            infoHousekeepingLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_103['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoHousekeepingLog,ServiceCheckConfig.Operation['splitSymbol'])

def runServiceCheckAvailability_104():            
    print "RUN Check ContinuesRun_EikonMon.py\n"
    if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile4'],ServiceCheckConfig.pathCRBAT) == False :
        #Notify ==> ContinuesRun_EikonMon.py isn't running
        infoEikonMon = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_104)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEikonMon,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> ContinuesRun_EikonMon.py is start recoverring
        infoEikonMon = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_104['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEikonMon,ServiceCheckConfig.Operation['splitSymbol'])
            
        if ServiceCheckRecovery.RecoveryRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile4']) == True :    
            if ServiceCheckFunction.CheckRunningBAT(ServiceCheckConfig.nameFileBAT['nameFile4'],ServiceCheckConfig.pathCRBAT) == True :
                #Notify ==> ContinuesRun_EikonMon.py recoverred successful
                infoEikonMon = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_104['complete'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEikonMon,ServiceCheckConfig.Operation['splitSymbol'])
            else :
                #Notify ==> ContinuesRun_EikonMon.py recoverred not successful
                infoEikonMon = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_104['fail'])
                ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEikonMon,ServiceCheckConfig.Operation['splitSymbol'])
        else:   
            #Notify ==> ContinuesRun_EikonMon.py recoverred not successful
            infoEikonMon = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_104['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEikonMon,ServiceCheckConfig.Operation['splitSymbol'])       
            
def runServiceCheckAvailability_105():
    print "RUN Check TsiLoadTest.exe\n"
    if ServiceCheckFunction.CheckEXEInTask(ServiceCheckConfig.FileTsiLoadTest,ServiceCheckConfig.waitTimeCEXEIT) == False :
        #Notify ==> TsiLoadTest.exe isn't running
        infoEXEInTask = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_105)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEXEInTask,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> TsiLoadTest.exe is start recoverring
        infoEXEInTask = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_105['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEXEInTask,ServiceCheckConfig.Operation['splitSymbol'])

        ServiceCheckRecovery.RecoveryEXEInTask(ServiceCheckConfig.FileTsiLoadTest,ServiceCheckConfig.nameFileBAT['nameFile4'],ServiceCheckConfig.pathCRBAT)
            
        if ServiceCheckFunction.CheckEXEInTask(ServiceCheckConfig.FileTsiLoadTest,ServiceCheckConfig.waitTimeCEXEIT) == True :
            #Notify ==> TsiLoadTest.exe recoverred successful
            infoEXEInTask = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_105['complete'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEXEInTask,ServiceCheckConfig.Operation['splitSymbol'])
        else:
            #Notify ==> TsiLoadTest.exe recoverred not successful
            infoEXEInTask = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_105['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoEXEInTask,ServiceCheckConfig.Operation['splitSymbol'])

def runServiceCheckAvailability_106():
    print "RUN Check Sensu-Client-Service\n"
    if ServiceCheckFunction.CheckStatusService (ServiceCheckConfig.nameService) == False :
        #Notify ==> Sensu-Client-Service isn't running
        infoStatusService = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_106)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoStatusService,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> Sensu-Client-Service is start recoverring
        infoStatusService = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_106['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoStatusService,ServiceCheckConfig.Operation['splitSymbol'])
            
        ServiceCheckRecovery.RecoveryStatusService(ServiceCheckConfig.nameService)
            
        if ServiceCheckFunction.CheckStatusService (ServiceCheckConfig.nameService) == True :
            #Notify ==> Sensu-Client-Service recoverred successful
            infoStatusService = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_106['complete'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoStatusService,ServiceCheckConfig.Operation['splitSymbol'])
        else:
            #Notify ==> Sensu-Client-Service recoverred not successful
            infoStatusService = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_106['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoStatusService,ServiceCheckConfig.Operation['splitSymbol'])

def runServiceCheckAvailability_107():
    print "RUN Check since-db1-e2e-perf.yaml\n"        
    if ServiceCheckFunction.CheckSinceYaml (ServiceCheckConfig.pathCSY,ServiceCheckConfig.waitTimeCSY) == False :
        #Notify ==> since-db1-e2e-perf.yaml isn't changing
        infoSinceYaml = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_107)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSinceYaml,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> since-db1-e2e-perf.yaml is start recoverring
        infoSinceYaml = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_107['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSinceYaml,ServiceCheckConfig.Operation['splitSymbol'])
            
        ServiceCheckRecovery.RecoverySinceYaml(ServiceCheckConfig.nameService)
            
        if ServiceCheckFunction.CheckSinceYaml (ServiceCheckConfig.pathCSY,ServiceCheckConfig.waitTimeCSY) == True :
            #Notify ==> since-db1-e2e-perf.yaml recoverred successful
            infoSinceYaml = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_107['complete'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSinceYaml,ServiceCheckConfig.Operation['splitSymbol'])
        else:
            #Notify ==> since-db1-e2e-perf.yaml recoverred not successful
            infoSinceYaml = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_107['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSinceYaml,ServiceCheckConfig.Operation['splitSymbol'])

def runServiceCheckAvailability_108():
    print "RUN Check sensu-client.log\n"        
    if ServiceCheckFunction.CheckSensuLog (ServiceCheckConfig.pathCSL,ServiceCheckConfig.waitTimeCSL) == False :
        #Notify ==> sensu-client.log isn't changing
        infoSensuLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.falseMsg_108)
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSensuLog,ServiceCheckConfig.Operation['splitSymbol'])
        #Notify ==> sensu-client.log is start recoverring
        infoSensuLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_108['start'])
        ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSensuLog,ServiceCheckConfig.Operation['splitSymbol'])
            
        ServiceCheckRecovery.RecoverySensuLog (ServiceCheckConfig.pathCSL,ServiceCheckConfig.nameService)
            
        if ServiceCheckFunction.CheckSensuLog (ServiceCheckConfig.pathCSL,ServiceCheckConfig.waitTimeCSL) == True :
            #Notify ==> sensu-client.log recoverred successful
            infoSensuLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['recoverySeverity'],ServiceCheckConfig.recoveryMsg_108['complete'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSensuLog,ServiceCheckConfig.Operation['splitSymbol'])
        else:
            #Notify ==> sensu-client.log recoverred not successful
            infoSensuLog = infoServiceCheckAvailability(ServiceCheckConfig.Operation['severity'],ServiceCheckConfig.recoveryMsg_108['fail'])
            ServiceCheckFunction.generateReportLog_version2(ServiceCheckConfig.pathOperation,ServiceCheckConfig.Operation['logname'],infoSensuLog,ServiceCheckConfig.Operation['splitSymbol'])
            
def ServiceCheckAvailability():
    runServiceCheckAvailability_101()
    runServiceCheckAvailability_102()                       
    runServiceCheckAvailability_104()             
    thread.start_new_thread(runServiceCheckAvailability_105,())          
    runServiceCheckAvailability_106()             
    thread.start_new_thread(runServiceCheckAvailability_107,())             
    thread.start_new_thread(runServiceCheckAvailability_108,())
               
if __name__ == '__main__':
    ServiceCheckAvailability()
