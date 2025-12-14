import argparse
from pathlib import Path

# Your banner tools
from pyfiglet import Figlet
from rich.console import Console

console = Console()

def show_banner():
    fig = Figlet(font="ansi_shadow")
    text = fig.renderText("Incident Response Tool")
    console.print(f"[bold #00ff66]{text}[/bold #00ff66]")


# IMPORT YOUR MODULES
from modules.systemInfo import SystemInfo
from modules.processScanner import ProcessScanner
from modules.NetworkMonitor import NetworkMonitor
from modules.LogCollector import LogCollector
from modules.HashFile import HashFile
from modules.ReportGenerator import ReportGenerator


def make_output_folder():
    out = Path("output")
    out.mkdir(exist_ok=True)
    return out


def main():
    # Always show banner first
    show_banner()

    parser = argparse.ArgumentParser(description="Incident Response Automation Tool", add_help=False)  # Disable default help printing
   
    parser.add_argument("--full", action="store_true", help="Run full scan (all modules)")
    parser.add_argument("--system", action="store_true", help="Collect system information")
    parser.add_argument("--processes", action="store_true", help="Scan processes for suspicious activity")
    parser.add_argument("--network", action="store_true", help="Scan network connections")
    parser.add_argument("--logs", action="store_true", help="Collect logs")
    parser.add_argument("--hash", type=str, help="Hash a file or folder")
    args = parser.parse_args()

     # If no arguments are provided, show options
    if not any(vars(args).values()):
        # print("[+] No arguments provided. Please choose one of the options below:")
      print("options:")
      print("  --full                Run full scan (all modules)")
      print("  --system              Collect system information")
      print("  --processes           Scan processes for suspicious activity")
      print("  --network             Scan network connections")
      print("  --logs                Collect logs")
      print("  --hash HASH           Hash a file or folder")
      return

    output = make_output_folder()
    final_data = {}

    # Handle arguments normally
    if args.full:
        print("[+] Running FULL scan...")
        
        system = SystemInfo()
        final_data["system"] = system.collectInfo()
        final_data["processes"] = ProcessScanner().scanProcesses()
        final_data["network"] = NetworkMonitor().scanConnections()
        final_data["logs"] = LogCollector().collectLogs(output_folder=output)

        rep = ReportGenerator()
        rep.save_json(final_data, output)
        rep.save_html(final_data, output)
        print("[+] Report saved in /output")
        return

    if args.system:
        print("[+] Running SYSTEM info...")
        system = SystemInfo()
        print(system.collectInfo())

    if args.processes:
        print("[+] Running PROCESS scan...")
        print(ProcessScanner().scanProcesses()["all_suspicious_Process"])

    if args.network:
        print("[+] Running NETWORK scan...")
        print(NetworkMonitor().scanconnections()["all_suspicious_connections"])

    if args.logs:
        print("[+] Collecting LOGS...")
        print(LogCollector().collectLogs(output_folder=output))

    if args.hash:
        print(f"[+] Hashing: {args.hash}")
        h = HashFile()
        target = args.hash
        if Path(target).is_file():
            print(h.hash_file(target))
        else:
            print(h.hash_folder(target))
if __name__ == "__main__":
    main()
