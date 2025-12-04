"""
What it does in the real world:
 This module collects basic information about a computer.
 It tells you what operating system is running, how long the machine has been on, how much CPU and RAM it’s using, and who is logged in.

Why it's useful in cybersecurity:
 Attackers sometimes change system settings or run the machine under heavy load.
 During an investigation, you need a quick summary to understand the machine’s status.

Example real-world use:
=>Check if the system is under stress (possible malware)

=>Identify unauthorized users logged in

=>Know how long the system has been running (helpful for timeline analysis)

"""

import platform  # try to retrieve system information
import psutil    # for system and process utilities
import datetime  # For handling date and time

class SystemInfo:
   #This module collects basic system information

    def collectInfo(self):
        #empty map for holding information
        info={}
        
        #Assign Operating system info into the map
        info["operating_system"]=platform.system()  # this function return OS name like windows, linux, etc.
        info["operating_system_version"]=platform.version() # this function return system version
        info["hostname"]=platform.node()  # this function return hostname of the machine
        
        #Assign hardware info like CPU and Ram into the map
        info["cpu_usage"]=psutil.cpu_percent(interval=1)  # this function return CPU usage percentage
        memoryview=psutil.virtual_memory() #Return about system memory usage 
        info["total_memory"]=memoryview.total
        info["used_memory"]=memoryview.used
        info["percent_memory"]=memoryview.percent

        #Assign spend time info into the map
         # this function return the system boot time
        boot_time=datetime.datetime.fromtimestamp(psutil.boot_time())
        # show the current time
        current_time=datetime.datetime.now
        
        #Calculate the time spent since boot
        spend_time=current_time()-boot_time
        info["uptime"]=str(spend_time)

        #Assign logged in users info into the list
        users=[]
        for user in psutil.users():
            users.append({"name": user.name,"started":str(user.started)})  # this function return the list of logged in users
        info["logged_in_users"]=users

        return info