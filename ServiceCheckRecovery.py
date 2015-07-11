import subprocess
import os

import ServiceCheckConfig

def RecoveryRunningBAT(filename):
    if filename == "AnalysisTestResult" :
        path = ServiceCheckConfig.pathRecoveryAnalysisTestResult
        if os.path.exists(path) == True :
            #command = r'c:\python26\python.exe ' + path
            command = r'start "Command Prompt" call c:\python26\python.exe ' + path
            #subprocess.Popen(command,cwd = r'D:\PostProcess\Script',creationflags=subprocess.CREATE_NEW_CONSOLE)
            os.system(command)
            return True
        else:
            return False

    elif filename == "zipTSILog" :
        path = ServiceCheckConfig.pathRecoveryzipTSILog
        if os.path.exists(path) == True :
            #command = r'c:\python26\python.exe ' + path
            command = r'start "Command Prompt" call c:\python26\python.exe ' + path
            #subprocess.Popen(command)
            os.system(command)
            return True
        else:
            return False

    elif filename == "HousekeepingLog" :
        path = ServiceCheckConfig.pathRecoveryHousekeepingLog
        if os.path.exists(path) == True :
            #command = r'c:\python26\python.exe ' + path
            command = r'start "Command Prompt" call c:\python26\python.exe ' + path
            #subprocess.Popen(command)
            os.system(command)
            return True
        else:
            return False

    elif filename == "ContinuesRun_EikonMon" :
        path = ServiceCheckConfig.pathRecoveryEikonMon
        if os.path.exists(path) == True :
            #command = r'c:\python26\python.exe ' + path
            command = r'start "Command Prompt" call c:\python26\python.exe ' + path
            #subprocess.Popen(command)
            os.system(command)
            return True
        else:
            return False
            
def RecoveryEXEInTask(nameProcess,nameFileBAT,pathLogFileBAT):
    cmdKillProcess = r"taskkill /f /im " + nameProcess
    pathLogFile = r""+ pathLogFileBAT + "\check" + nameFileBAT + ".log"
    if ServiceCheckFunction.CheckRunningBAT(nameFileBAT,pathLogFileBAT) == True : 
        processID = ServiceCheckFunction.readFindProcessID(pathLogFile)
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
    
    