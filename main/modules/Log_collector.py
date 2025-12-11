"""
This module collects important system logs (like auth logs and system logs).
Logs are stored in a safe folder so the investigator can review them later.

Why it's useful:
Logs contain evidence of:

failed logins

brute-force attempts

suspicious commands

system errors right before an attack

unauthorized access

Example real-world use:

Check if someone tried to break into the server

Find logs showing attacker activity

Preserve logs before they get overwritten
"""
import shutil
from pathlib import Path
import platform


class LogCollector:

    def __init__(self,output_folder):
        results=[]
        if platform.system()!="Linux":
            return ["Log collection works linux only"]
        
        logLists=[
            "/var/log/system.log",
            "/var/log/auth.log",
        ]

        for log in logLists:
            src = Path(log)
            if src.exists():
                dst = Path(output_folder) / src.name
                try:
                    shutil.copy2(src, dst)
                    results.append(f"Copied: {src}")
                except:
                    results.append(f"Failed: {src}")
            else:
                results.append(f"Not found: {src}")

        return results

# log=LogCollector("/path/to/safe/folder")
# log_results=log.__init__("/path/to/safe/folder")