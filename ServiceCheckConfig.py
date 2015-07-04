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
Operation = {'logname' : "Operation_E2ELog2GMI.log" , 'severity' : "CRITICAL" , 'splitSymbol' : "|"}
#pathOperation = r"D:\E2EPerformance\AppstatParser\logs\HanuLogs\E2ELog2GMI"
pathOperation = r"C:\Users\U6031187\Desktop"

#For Configure Property in Function CheckRunningBAT (1-2-3-4)
#pathCRBAT = r"D:\E2EPerformance\AppstatParser\logs\HanuLogs\E2ELog2GMI"
pathCRBAT = r"C:\Users\U6031187\Desktop\E2ELog2GMI"

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

# =============================== ServiceCheckResponseTime's Configuration ===============================
#For Configure Property in ServiceCheckResponseTime
Developer = {'logname' : "Developer_E2ELog2GMI.log" , 'severity' : "WARNING" , 'splitSymbol' : "|"}
#pathDeveloper = r"D:\E2EPerformance\AppstatParser\logs\HanuLogs\E2ELog2GMI"
pathDeveloper = r"C:\Users\U6031187\Desktop"

#For Configure Property in Function CheckResponseTime
limitTimeRP = { '10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 }
limitTimeEdge = { '10Minute' : 0 , '60Minute' : 0 , 'Daily' : 0 , 'Minute' : 0 , 'TAQCooked' : 0 , 'TASCooked' : 0 , 'TASRAW' : 0 , 'TickTAQ' : 0 , 'TickTAS' : 0 , 'Yearly' : 0 }


