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
        self.unknown_words = ["unknown", "powershell", "curl", "bash", "netcat", "wget"]

    def scanProcesses(self):
        all_processes = []
        suspicious_processes = []

#https://psutil.readthedocs.io/en/latest/#psutil.process_iter
        for proc in psutil.process_iter(["pid", "name", "username", "cmdline"]):
            try:
                pid = proc.info["pid"]
                name = proc.info["name"] or ""
                username = proc.info["username"]
                cmdline = proc.info.get("cmdline") or []

                data = {
                    "pid": pid,
                    "name": name,
                    "user": username,
                    "cmdline": cmdline
                }
                all_processes.append(data)

                # Check suspicious words in process name or command line
                found = False
                for word in self.unknown_words:
                    if word.lower() in name.lower():
                        found = True
                        break
                    # Check command line arguments
                    for arg in cmdline:
                        if word.lower() in arg.lower():
                            found = True
                            break
                    if found:
                        break

                if found:
                    suspicious_processes.append(data)

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        return {
            "all_process": all_processes,
            "all_suspicious_process": suspicious_processes
        }
# p1=ProcessScanner()
# print(p1.scanProcesses())
                