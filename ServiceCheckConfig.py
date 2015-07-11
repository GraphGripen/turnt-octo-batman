import socket

# =============================== General Configuration ===============================
#For Configure Property in Class ServiceInfo 
version = "CBE 1.0.2"
sourceComponentId = {'location' : socket.gethostname() , 'locationType' : "Hostname" , 'component' : "Apache 1.0.53" , 'subComponent' : "Authentication Engine" , 'componentIdType' : "Process" , 'componentType' : "Web Server" , 'application' : "FOAM Web Server" , 'instanceId' : 1 , 'processId' : 29018 , 'threadId' : 1 }
globalInstanceId = 0
situation = {'categoryName' : "ReportSituation" , 'situationType' : {'reasoningScope' : "INTERNAL" , 'reportCategory' : "SECURITY"}}
msgDataElement = {'msgId' : "FOAM_001099" , 'msgIdType' : "Reuters"}
repeatCount = 0
elapsedTime = 0
sequenceNumber = 0

# =============================== ServiceCheckAvailability's Configuration ===============================
#For Configure Property in ServiceCheckAvailability
Operation = {'logname' : "Operation_E2ELog2GMI.log" , 'severity' : "CRITICAL" , 'recoverySeverity' : "INFORMATION" ,'splitSymbol' : "|"}
#pathOperation = r"D:\E2EPerformance\AppstatParser\logs\HanuLogs\E2ELog2GMI"
pathOperation = r"C:\Users\U6031187\Desktop"

#For Configure Property in Function CheckRunningBAT (1-2-3-4)
#pathCRBAT = r"D:\E2EPerformance\AppstatParser\logs\HanuLogs\E2ELog2GMI"
pathCRBAT = r"C:\Users\U6031187\Desktop\E2ELog2GMI"
nameFileBAT = {'nameFile1' : "AnalysisTestResult" , 'nameFile2' : "zipTSILog" , 'nameFile3' : "HousekeepingLog" , 'nameFile4' : "ContinuesRun_EikonMon"}

#For Configure Property in Function CheckEXEInTask (5)
FileTsiLoadTest = "TsiLoadTest.exe"
waitTimeCEXEIT = 20

#For Configure Property in Function CheckStatusService (6)
nameService = "sensu-client"

#For Configure Property in Function CheckSinceYaml (7)
pathCSY = r"D:\E2EPerformance\AppstatParser\bin\since-db1-e2e-perf.yaml"
waitTimeCSY = 20

#For Configure Property in Function CheckSensuLog (8)
pathCSL = r"D:\eikon\monitoring\log\sensu\sensu-client.log"
waitTimeCSL = 20

#For Path File For File .BAT
pathRecoveryAnalysisTestResult = r'C:\Users\U6031187\Desktop\AAA\ETSVersionCheck\accepthostkeyCOVersion.bat'   #r'D:\E2EPerformance\Automation\RunE2E_EikonMon.bat'
pathRecoveryzipTSILog = r'D:\E2EPerformance\Automation\RunE2E_EikonMon.bat'
pathRecoveryHousekeepingLog = r'D:\E2EPerformance\Automation\RunE2E_EikonMon.bat'
pathRecoveryEikonMon = r'D:\E2EPerformance\Automation\RunE2E_EikonMon.bat'

#For Message in Each Checker (Default)
falseMsg_101 = "File AnalysisTestResult.py is downed"
falseMsg_102 = "File zipTSILog.py is downed"
falseMsg_103 = "File HousekeepingLog.py is downed"
falseMsg_104 = "File ContinuesRun_EikonMon.py is downed"
falseMsg_105 = "File TsiLoadTest.exe is downed"
falseMsg_106 = "Sensu-Client-Service is stopped"
falseMsg_107 = "File since-db1-e2e-perf.yaml is not changed"
falseMsg_108 = "File sensu-client.log is not changed"

#For Message in Each Checker (Recovery)
recoveryMsg_101 = {'start' : "Attemp Recovery File AnalysisTestResult.py" , 'complete' : "Recovery File AnalysisTestResult.py Success" , 'fail' : "Unable Recovery File AnalysisTestResult.py"}
recoveryMsg_102 = {'start' : "Attemp Recovery File zipTSILog.py" , 'complete' : "Recovery File zipTSILog.py Success" , 'fail' : "Unable Recovery File zipTSILog.py"}
recoveryMsg_103 = {'start' : "Attemp Recovery File HousekeepingLog.py" , 'complete' : "Recovery File HousekeepingLog.py Success" , 'fail' : "Unable Recovery File HousekeepingLog.py"}
recoveryMsg_104 = {'start' : "Attemp Recovery File ContinuesRun_EikonMon.py" , 'complete' : "Recovery File ContinuesRun_EikonMon.py Success" , 'fail' : "Unable Recovery File ContinuesRun_EikonMon.py"}
recoveryMsg_105 = {'start' : "Attemp Recovery File TsiLoadTest.exe" , 'complete' : "Recovery File TsiLoadTest.exe Success" , 'fail' : "Unable Recovery File TsiLoadTest.exe"}
recoveryMsg_106 = {'start' : "Attemp Recovery Sensu-Client-Service" , 'complete' : "Recovery Sensu-Client-Service Success" , 'fail' : "Unable Recovery Sensu-Client-Service"}
recoveryMsg_107 = {'start' : "Attemp Recovery since-db1-e2e-perf.yaml" , 'complete' : "Recovery since-db1-e2e-perf.yaml Success" , 'fail' : "Unable Recovery since-db1-e2e-perf.yaml"}
recoveryMsg_108 = {'start' : "Attemp Recovery sensu-client.log" , 'complete' : "Recovery sensu-client.log Success" , 'fail' : "Unable Recovery sensu-client.log"}


# =============================== ServiceCheckResponseTime's Configuration ===============================
#For Configure Property in ServiceCheckResponseTime
Developer = {'logname' : "Developer_E2ELog2GMI.log" , 'severity' : "WARNING" , 'splitSymbol' : "|"}
#pathDeveloper = r"D:\E2EPerformance\AppstatParser\logs\HanuLogs\E2ELog2GMI"
pathDeveloper = r"C:\Users\U6031187\Desktop"

#For Configure Property in Function CheckResponseTime
limitTimeRP = {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 }
limitTimeEdge = {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 }


