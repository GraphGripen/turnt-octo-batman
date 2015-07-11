from datetime import datetime
import os
import time
import wmi
import pythoncom

import ServiceCheckConfig

# =============================== General Function ============================= 
def getCurrentDateTime_version1():
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def getCurrentDateTime_version2():
    currentTime = datetime.now()
    currentmillisecond = currentTime.microsecond/1000
    outputTime = currentTime.strftime('%Y-%m-%dT%H:%M:%S') + "." + str(currentmillisecond)      
    return outputTime     

def ReadfileLog(path):
    f_in = open(path,"rb")
    lstOutput = []
    for line in f_in:
        lstOutput.append(line)
    f_in.close()
    return lstOutput

def generateReportLog_version1(path,fileLogName,info,splitSymbol) :
    if not os.path.exists(path):
        os.makedirs(path)
        
    path = os.path.join(path, fileLogName)
    
    if not os.path.exists(path):
        f_out = open(path,"wb")
        preheader = ["creationTime","version","severity","sourceComponentId.location","sourceComponentId.location","sourceComponentId.locationType","msg","globalInstanceId","sourceComponentId.component","sourceComponentId.subComponent","sourceComponentId.componentIdType","sourceComponentId.componentType","sourceComponentId.application","sourceComponentId.instanceId","sourceComponentId.processId","sourceComponentId.threadId","situation.categoryName","situation.situationType.reasoningScope","situation.situationType.reportCategory","msgDataElement.msgId","msgDataElement.msgIdType","repeatCount","elapsedTime","sequenceNumber"]
        header = splitSymbol.join(preheader) + '\r\n'
        f_out.write(header)
    else:
        f_out = open(path,"ab")
    
    content = []
    content.append(info.creationTime)
    content.append(info.version)
    content.append(info.severity)
    content.append(info.sourceComponentId['location'])
    content.append(info.sourceComponentId['locationType'])
    content.append(info.msg)
    content.append(str(info.globalInstanceId))
    content.append(info.sourceComponentId['component'])
    content.append(info.sourceComponentId['subComponent'])
    content.append(info.sourceComponentId['componentIdType'])
    content.append(info.sourceComponentId['componentType'])
    content.append(info.sourceComponentId['application'])
    content.append(str(info.sourceComponentId['instanceId']))
    content.append(str(info.sourceComponentId['processId']))
    content.append(str(info.sourceComponentId['threadId']))
    content.append(info.situation['categoryName'])
    content.append(info.situation['situationType']['reasoningScope'])
    content.append(info.situation['situationType']['reportCategory'])
    content.append(info.msgDataElement['msgId'])
    content.append(info.msgDataElement['msgIdType'])
    content.append(str(info.repeatCount))
    content.append(str(info.elapsedTime))
    content.append(str(info.sequenceNumber))
    
    output = splitSymbol.join(content) + '\r\n'
    f_out.write(output)
    f_out.close()   

def generateReportLog_version2(path,fileLogName,info,splitSymbol) :   
    if not os.path.exists(path):
        os.makedirs(path)
        
    path = os.path.join(path, fileLogName)
    
    if not os.path.exists(path):
        f_out = open(path,"wb")
        detailLog = ""
        f_out.write(detailLog)
    else:
        f_out = open(path,"ab")    

    content = []
    content.append('{"' + "timestamp" + '":'+'"' + info.creationTime + '"')
    content.append('"' + "msg_severity"  + '":'+'"' + info.severity + '"')
    content.append('"' + "message"  + '":'+'"' + info.msg + '"')

    output = splitSymbol.join(content) + '\r\n'
    f_out.write(output)
    f_out.close()   

def readFindProcessID(path):
    f_in = open(path,"rb")
    output = ""
    for line in f_in:
        if(line.find("cmd.exe") != -1 ):
           output = line
    f_in.close()
    detail = output.split()
    return detail[1]
    
# =============================== ServiceCheckAvailability's Function =============================  
def CheckRunningBAT(filename,destinationLog):
    #Begin
    command = r'tasklist /fi "windowtitle eq Command Prompt - c:\Python26\python.exe ' + filename + '.py">' + destinationLog + '\check' + filename + '.log' 
    filepath = r""+ destinationLog + '\check'+ filename + ".log"
    os.system(command)
    contentLog = ReadfileLog(filepath)
    for data in contentLog :
        if data.find("No tasks are running") != -1 :
            return False
    return True
   
def CheckEXEInTask (nameProcess,waitTime):
    pythoncom.CoInitialize()
    #Before
    task = wmi.WMI ()
    countTsiLoadTestBefore = len(task.Win32_Process (name = nameProcess))
    #Wait
    time.sleep(waitTime)
    #After
    task = wmi.WMI ()
    countTsiLoadTestAfter = len(task.Win32_Process (name = nameProcess))
    print "countTsiLoadTestBefore : " + str(countTsiLoadTestBefore)
    print "countTsiLoadTestAfter : " + str(countTsiLoadTestAfter)
    pythoncom.CoUninitialize()
    #Check
    if (countTsiLoadTestBefore != countTsiLoadTestAfter) :
        if countTsiLoadTestBefore != 0 or countTsiLoadTestAfter != 0 :
            return True
        return False  
    return False
    
def CheckStatusService (nameservice):
    #Begin
    service = wmi.WMI ()
    detailService = service.Win32_Service (name = nameservice)
    if len(detailService) == 0 :
        return False
    else :
        if detailService[0].State == "Running" :
            return True
    return False
    
def CheckSinceYaml (path,waitTime):
    #Before
    yamlContentBefore = ReadfileLog (path)
    #Wait
    time.sleep(waitTime)
    #After
    yamlContentAfter = ReadfileLog (path)
    #Check
    lengthyamlContentBefore = len(yamlContentBefore)
    lengthyamlContentAfter = len(yamlContentAfter)
    count = 0
    
    if lengthyamlContentBefore != lengthyamlContentAfter :
        return True
    else :
        while count < lengthyamlContentAfter :
            dataBefore = yamlContentBefore[count]
            dataAfter = yamlContentAfter[count]
            
            if dataBefore != dataAfter :
                return True
            count += 1
    return False
            
def CheckSensuLog (path,waitTime):
    #Before
    statinfo = os.stat(path)
    sizeBefore = statinfo.st_size
    #Wait
    time.sleep(waitTime)
    #After
    statinfo = os.stat(path)
    sizeAfter = statinfo.st_size
    #Check
    print sizeBefore
    print sizeAfter
    if sizeBefore != sizeAfter and sizeBefore < sizeAfter :
        return True
    return False

# =============================== ServiceCheckResponseTime's Function =============================
def CheckResponseTime (type,interval,time):
    if type == "RP" :
        limitTime = ServiceCheckConfig.limitTimeRP[interval]
    elif type == "Edge" :
        limitTime = ServiceCheckConfig.limitTimeEdge[interval]
    
    if time < limitTime :
        return True 
    return False
     
if __name__ == '__main__':
    print "Reuters"
    