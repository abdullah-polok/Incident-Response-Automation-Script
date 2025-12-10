
"""
This module checks all active internet/network connections on the system.
It shows open ports, remote IPs, and identifies dangerous ports commonly used by attackers.

Why it's useful:
Hacked systems often have:

reverse shells sending data back to the attacker

backdoor ports opened secretly

strange IP addresses connected

Example real-world use:

See if the machine is connected to a suspicious IP

Detect reverse shell ports like 4444

Monitor for hidden communication channels
"""

import psutil

class NetworkMonitor:
    def __init__(self):
        self.unknown_ports=[5555,4444,13327,31337,12345,54321,9999]
    def scanconnections(self):
        all_connections=[]
        suspicious_connections=[]

        #https://psutil.readthedocs.io/en/latest/#psutil.Process.net_connections
        for connect in psutil.net_connections():
            data={
                "pid":connect.pid,
                "local_address":f"{connect.laddr.port}" if connect.laddr else "N/A",
                "remote_address":f"{connect.raddr.ip}:{connect.raddr.port}" if connect.raddr else "N/A",
                "status":connect.status
            }
            all_connections.append(data)
            # Check for suspicious ports
            if connect.laddr and connect.laddr.port in self.unknown_ports:
                suspicious_connections.append(data)
        return {
           "All Connections":all_connections,
           "All suspicious Connections": suspicious_connections
       }