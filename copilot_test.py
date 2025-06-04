import os
import platform

def print_system_uptime():
    if platform.system() == "Windows":
        # On Windows, use 'net statistics workstation'
        import subprocess
        output = subprocess.check_output("net statistics workstation", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                print("System uptime (Windows):", line)
                break
    else:
        # On Unix/Linux, read from /proc/uptime
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_hours = uptime_seconds // 3600
            uptime_minutes = (uptime_seconds % 3600) // 60
            print(f"System uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes")

if __name__ == "__main__":
    print_system_uptime()
