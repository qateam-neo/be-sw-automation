
import sys
import os
import platform

class System_Path_Backend():
    Platform=platform.platform()

    if "macos" in  Platform.lower():
        Platform= "mac"
    elif "windows" in Platform.lower():
        Platform="windows"

    System_Path=sys.path

    if Platform == "mac":  
        Path= os.getcwd() + "/Appium-Automation-Python"
        Files=os.listdir(Path)
        # print(Files)
        for File in Files:
            # print(os.path.isdir(File))
            if "." not in File:  
                sys.path.append(Path+"/"+File)


    if Platform == "windows":  
        # Path= os.getcwd() 
        # while Path.endswith("Appium-Automation-Python")==False and Path.endswith("Appium Automation Python")==False:
        #     Path=Path[:-1]
        #     # print(Path)
        
        # print("Final Path: " + Path)
        # Files=os.listdir(Path)
        # print(Files)
        # for File in Files:
        #     if os.path.isdir(File) and File[0]!=".":  
        #         if Path+"\\"+File not in System_Path:
        #             sys.path.append(Path+"\\"+File)
        
        
        #TEMPORARY FOR PYTEST#
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\API_Flows")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\ApplicationFlows")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\FailedScreenshots")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\FullFlows")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\GUI")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\ScreensAndMethod")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\TechnicalFlows")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\Admin")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\smoke")
        sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\specific_scenarios")
                        
            
    # print (sys.path)