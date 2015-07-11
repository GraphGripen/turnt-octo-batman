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
Operation = {'logname' : "Operation.log" , 'severity' : "CRITICAL" , 'recoverySeverity' : "INFORMATION" ,'splitSymbol' : ","}
#pathOperation = r"D:\E2EPerformance\E2EMonitoring\Log"
pathOperation = r"C:\Users\U6031187\Desktop"

#For Configure Property in Function CheckRunningBAT (1-2-3-4)
#pathCRBAT = r"D:\E2EPerformance\E2EMonitoring\Log\temp"
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

#For Path File For File .py
pathRecoveryAnalysisTestResult = r'D:\PostProcess\Script\AnalysisTestResult.py'
pathRecoveryzipTSILog = r'D:\PostProcess\Script\zipTSILog.py'
pathRecoveryHousekeepingLog = r'D:\PostProcess\Script\HousekeepingLog.py'
pathRecoveryEikonMon = r'D:\PostProcess\Script\ContinuesRun_EikonMon.py'

#For Message in Each Checker (Default)
falseMsg_101 = "File AnalysisTestResult.py isn't running"
falseMsg_102 = "File zipTSILog.py isn't running"
falseMsg_103 = "File HousekeepingLog.py isn't running"
falseMsg_104 = "File ContinuesRun_EikonMon.py isn't running"
falseMsg_105 = "File TsiLoadTest.exe isn't running"
falseMsg_106 = "Sensu-Client-Service is stopped"
falseMsg_107 = "File since-db1-e2e-perf.yaml is not changed"
falseMsg_108 = "File sensu-client.log is not changed"

#For Message in Each Checker (Recovery)
recoveryMsg_101 = {'start' : "Attemping recover File AnalysisTestResult.py" , 'complete' : "Recovery File AnalysisTestResult.py is success" , 'fail' : "Unable recover File AnalysisTestResult.py"}
recoveryMsg_102 = {'start' : "Attemping recover File zipTSILog.py" , 'complete' : "Recovery File zipTSILog.py is success" , 'fail' : "Unable recover File zipTSILog.py"}
recoveryMsg_103 = {'start' : "Attemping recover File HousekeepingLog.py" , 'complete' : "Recovery File HousekeepingLog.py is success" , 'fail' : "Unable recover File HousekeepingLog.py"}
recoveryMsg_104 = {'start' : "Attemping recover File ContinuesRun_EikonMon.py" , 'complete' : "Recovery File ContinuesRun_EikonMon.py is success" , 'fail' : "Unable recover File ContinuesRun_EikonMon.py"}
recoveryMsg_105 = {'start' : "Attemping recover File TsiLoadTest.exe" , 'complete' : "Recovery File TsiLoadTest.exe is success" , 'fail' : "Unable recover File TsiLoadTest.exe"}
recoveryMsg_106 = {'start' : "Attemping recover Sensu-Client-Service" , 'complete' : "Recovery Sensu-Client-Service is success" , 'fail' : "Unable recover Sensu-Client-Service"}
recoveryMsg_107 = {'start' : "Attemping recover since-db1-e2e-perf.yaml" , 'complete' : "Recovery since-db1-e2e-perf.yaml is success" , 'fail' : "Unable recover since-db1-e2e-perf.yaml"}
recoveryMsg_108 = {'start' : "Attemping recover sensu-client.log" , 'complete' : "Recovery sensu-client.log is success" , 'fail' : "Unable recover sensu-client.log"}

#For Time to Wait in 1 all checkers(Loop)
waitTimeAll = max(waitTimeCSL,waitTimeCSY,waitTimeCEXEIT) + 5

# =============================== ServiceCheckResponseTime's Configuration ===============================
#For Configure Property in ServiceCheckResponseTime
Developer = {'logname' : "Developer.log" , 'severity' : "WARNING" , 'splitSymbol' : "|"}
#pathDeveloper = r"D:\E2EPerformance\AppstatParser\logs\HanuLogs\E2ELog2GMI"
pathDeveloper = r"D:\E2EPerformance\E2EMonitoring\Log"

#For Configure Property in Function CheckResponseTime
serverSTC = { 'limitTimeRP' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } , 'limitTimeEdge' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } }
serverNTC = { 'limitTimeRP' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } , 'limitTimeEdge' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } }
serverHDC = { 'limitTimeRP' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } , 'limitTimeEdge' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } }
serverDTC = { 'limitTimeRP' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } , 'limitTimeEdge' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } }



