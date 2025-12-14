"""
This module looks at every program (process) running on the system.
It also checks whether any running program looks suspicious or unusual.

Why it's useful:
Malware or hackers often run strange processes like:

###hidden PowerShell

###reverse shells

###tools like curl/wget for downloading files

###unknown custom binaries

This module helps investigators quickly spot these.

Example real-world use:

Detect a hacker running nc (netcat)

Find malware pretending to be a normal program

Spot unusual commands running in the background
"""

import psutil # for system and process utilities

class ProcessScanner:
    def __init__(self):
        self.unknown_words=["unknown","powershell","curl","bash","netcat","wget"]  # List of known suspicious process names

    def scanProcesses(self):
            all_processes=[]
            suspicious_processes=[]

            #https://psutil.readthedocs.io/en/latest/#psutil.process_iter
            
            for process in psutil.process_iter(["pid", "name","username"]):
               data={
                    "pid:":process.info["pid"],
                    "name":process.info["name"],
                    "user":process.info["username"]
               }
               all_processes.append(data)   

               #check the process name is suspicious
               for word in self.unknown_words:
                    if word in data["name"]:
                         suspicious_processes.append(data)

            return { "All Process:":all_processes,
                     "All Suspicious Process":suspicious_processes
                     }      


# p1=ProcessScanner()
# print(p1.scanProcesses())
                