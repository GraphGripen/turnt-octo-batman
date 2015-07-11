import subprocess
import os

import ServiceCheckConfig
import ServiceCheckAvailability

def RecoveryRunningBAT(filename):
    if filename == "AnalysisTestResult" :
        path = ServiceCheckConfig.pathRecoveryAnalysisTestResult
        if os.path.exists(path) == True :
            command = r'c:\python26\python.exe ' + path
            subprocess.Popen(command)
            return True
        else:
            return False
        
        print "AnalysisTestResult"

    elif filename == "zipTSILog" :
        path = ServiceCheckConfig.pathRecoveryzipTSILog
        if os.path.exists(path) == True :
            command = r'c:\python26\python.exe ' + path
            subprocess.Popen(command)
            return True
        else:
            return False
        
        print "zipTSILog"

    elif filename == "HousekeepingLog" :
        path = ServiceCheckConfig.pathRecoveryHousekeepingLog
        if os.path.exists(path) == True :
            command = r'c:\python26\python.exe ' + path
            subprocess.Popen(command)
            return True
        else:
            return False
            
        print "HousekeepingLog"

    elif filename == "ContinuesRun_EikonMon" :
        path = ServiceCheckConfig.pathRecoveryEikonMon
        if os.path.exists(path) == True :
            command = r'c:\python26\python.exe ' + path
            subprocess.Popen(command)
            return True
        else:
            return False
            
        print "ContinuesRun_EikonMon"
            
def RecoveryEXEInTask(nameProcess,nameFileBAT,pathLogFileBAT):
    cmdKillProcess = r"taskkill /f /im " + nameProcess
    if ServiceCheckFunction.CheckRunningBAT(nameFileBAT,pathLogFileBAT) == True : 
        processID = ServiceCheckFunction.readFindProcessID(pathLogFileBAT)
        cmdKillEikonMon = r"taskkill /pid " + str(processID)
        os.system(cmdKillEikonMon)
        os.system(cmdKillProcess)
        RecoveryRunningBAT(nameFileBAT)
    else:
        os.system(cmdKillProcess)
        RecoveryRunningBAT(nameFileBAT)
    
def RecoveryStatusService(nameservice):
    command = "net start " + nameservice
    os.system(command)
        
def RecoverySinceYaml(nameservice):
    commandStop = "net stop " + nameservice
    commandStart = "net start " + nameservice
    os.system(commandStop)
    os.system(commandStart)
    
def RecoverySensuLog (path,nameservice):
    commandStop = "net stop " + nameservice
    commandStart = "net start " + nameservice
    os.system(commandStop)
    
    if os.path.exists(path) == True :
        os.remove(path)
            
    os.system(commandStart)
    
if __name__ == '__main__':
    print "Reuters" 
    
    