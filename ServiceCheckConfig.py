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
Operation = {'logname' : "Operation.log" , 'severity' : "CRITICAL" , 'recoverySeverity' : "INFORMATION" ,'splitSymbol' : "," , 'logFileSize' : 5*1024*1024 }
pathOperation = r"D:\E2EPerformance\E2EMonitoring\Log"

#For Configure Property in Function CheckRunningBAT (101-102-103)
pathCRBAT = r"D:\E2EPerformance\E2EMonitoring\Log\temp"
nameFileBAT = {'nameFile1' : "AnalysisTestResult" , 'nameFile2' : "zipTSILog" , 'nameFile3' : "ContinuesRun_EikonMon"}

#For Configure Property in Function CheckEXEInTask (104)
FileTsiLoadTest = "TsiLoadTest.exe"
waitTimeCEXEIT = 30

#For Configure Property in Function CheckStatusService (105)
nameService = "sensu-client"

#For Configure Property in Function CheckSinceYaml (106)
pathCSY = r"D:\E2EPerformance\AppstatParser\bin\since-db1-e2e-perf.yaml"
waitTimeCSY = 60

#For Configure Property in Function CheckSensuLog (107)
pathCSL = r"D:\eikon\monitoring\log\sensu\sensu-client.log"
waitTimeCSL = 40

#For Path File For File .py
pathRecoveryAnalysisTestResult = r'D:\PostProcess\Script\AnalysisTestResult.py'
pathRecoveryzipTSILog = r'D:\PostProcess\Script\zipTSILog.py'
pathRecoveryHousekeepingLog = r'D:\PostProcess\Script\HousekeepingLog.py'
pathRecoveryEikonMon = r'D:\PostProcess\Script\ContinuesRun_EikonMon.py'

#For Message in Each Checker (Default)
falseMsg_101 = "File AnalysisTestResult.py isn't running"
falseMsg_102 = "File zipTSILog.py isn't running"
falseMsg_103 = "File ContinuesRun_EikonMon.py isn't running"
falseMsg_104 = "File TsiLoadTest.exe isn't running"
falseMsg_105 = "Sensu-Client-Service is stopped"
falseMsg_106 = "File since-db1-e2e-perf.yaml is not changed"
falseMsg_107 = "File sensu-client.log is not changed"

#For Message in Each Checker (Recovery)
recoveryMsg_101 = {'start' : "Attemping recover File AnalysisTestResult.py" , 'complete' : "Recovery File AnalysisTestResult.py is success" , 'fail' : "Unable recover File AnalysisTestResult.py"}
recoveryMsg_102 = {'start' : "Attemping recover File zipTSILog.py" , 'complete' : "Recovery File zipTSILog.py is success" , 'fail' : "Unable recover File zipTSILog.py"}
recoveryMsg_103 = {'start' : "Attemping recover File ContinuesRun_EikonMon.py" , 'complete' : "Recovery File ContinuesRun_EikonMon.py is success" , 'fail' : "Unable recover File ContinuesRun_EikonMon.py"}
recoveryMsg_104 = {'start' : "Attemping recover File TsiLoadTest.exe" , 'complete' : "Recovery File TsiLoadTest.exe is success" , 'fail' : "Unable recover File TsiLoadTest.exe"}
recoveryMsg_105 = {'start' : "Attemping recover Sensu-Client-Service" , 'complete' : "Recovery Sensu-Client-Service is success" , 'fail' : "Unable recover Sensu-Client-Service"}
recoveryMsg_106 = {'start' : "Attemping recover since-db1-e2e-perf.yaml" , 'complete' : "Recovery since-db1-e2e-perf.yaml is success" , 'fail' : "Unable recover since-db1-e2e-perf.yaml"}
recoveryMsg_107 = {'start' : "Attemping recover sensu-client.log" , 'complete' : "Recovery sensu-client.log is success" , 'fail' : "Unable recover sensu-client.log"}

#For Time to Wait in 1 all checkers(Loop)
waitTimeAll = max(waitTimeCSL,waitTimeCSY,waitTimeCEXEIT) + 10

# =============================== ServiceCheckResponseTime's Configuration ===============================
#For Configure Property in ServiceCheckResponseTime
Developer = {'logname' : "Developer.log" , 'severity' : "WARNING" , 'splitSymbol' : "," , 'logFileSize' : 5*1024*1024 }
pathDeveloper = r"D:\E2EPerformance\E2EMonitoring\Log"

#For Configure Property in Function CheckResponseTime
serverSTC = { 'limitTimeRP' : {'10Minute' : 0.7 , '60Minute' : 1 , 'Daily' : 0.5 , 'Minute' : 0.5 , 'TAQCooked' : 2 , 'TASCooked' : 1.5 , 'TASRAW' : 2 , 'TickTAQ' : 0.5 , 'TickTAS' : 0.5 , 'Yearly' : 1 } , 'limitTimeEdge' : {'10Minute' : 0.7 , '60Minute' : 1 , 'Daily' : 0.5 , 'Minute' : 0.5 , 'TAQCooked' : 2 , 'TASCooked' : 1.5 , 'TASRAW' : 2 , 'TickTAQ' : 0.5 , 'TickTAS' : 0.5 , 'Yearly' : 1 } }
serverNTC = { 'limitTimeRP' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } , 'limitTimeEdge' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } }
serverHDC = { 'limitTimeRP' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } , 'limitTimeEdge' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } }
serverDTC = { 'limitTimeRP' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } , 'limitTimeEdge' : {'10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 } }

