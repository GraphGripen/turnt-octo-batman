import subprocess
import thread
import os

import ServiceCheckConfig
import ServiceCheckAvailability

def RecoveryRunningBAT(filename):
    if filename == "AnalysisTestResult" :
        path = ServiceCheckConfig.pathRecoveryAnalysisTestResult
        if os.path.exists(path) == False :
            createFile = open(path,"wb")
            createFile.write("")
            createFile.close()
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
        else:
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
        
        print "AnalysisTestResult"

    elif filename == "zipTSILog" :
        path = ServiceCheckConfig.zipTSILog
        if os.path.exists(path) == False :
            createFile = open(path,"wb")
            createFile.write("")
            createFile.close()
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
        else:
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
        
        print "zipTSILog"

    elif filename == "HousekeepingLog" :
        path = ServiceCheckConfig.HousekeepingLog
        if os.path.exists(path) == False :
            createFile = open(path,"wb")
            createFile.write("")
            createFile.close()
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
        else:
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
            
        print "HousekeepingLog"

    elif filename == "ContinuesRun_EikonMon" :
        path = ServiceCheckConfig.EikonMon
        if os.path.exists(path) == False :
            createFile = open(path,"wb")
            createFile.write("")
            createFile.close()
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
        else:
            subprocess.Popen(path, cwd=r"C:\Users\U6031187\Desktop\AAA\ETSVersionCheck")
            
        print "ContinuesRun_EikonMon"
            
def RecoveryEXEInTask(nameProcess,nameFileBAT):
    cmdKillProcess = r"taskkill /f /im " + nameProcess
    os.system(cmdKillProcess)
    RecoveryRunningBAT(nameFileBAT)
    return "AAAA"
    
def RecoveryStatusService(nameservice):
    command = "net start " + nameservice
    os.system(command)
        
def RecoverySinceYaml(nameservice):
    commandStop = "net stop " + nameservice
    commandStart = "net start " + nameservice
    os.system(commandStop)
    os.system(commandStart)
    
def RecoverySensuLog (path,nameservice)
    commandStop = "net stop " + nameservice
    commandStart = "net start " + nameservice
    os.system(commandStop)
    
    if os.path.exists(path) == False :
        createFile = open(path,"wb")
        createFile.write("")
        createFile.close()
    else:
        os.remove(path)
        createFile = open(path,"wb")
        createFile.write("")
        createFile.close()
    
    os.system(commandStart)
    
if __name__ == '__main__':
    print "Reuters" 
    
    
    