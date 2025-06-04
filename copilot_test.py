import platform
import subprocess

def get_windows_uptime():
    try:
        result = subprocess.run(
            ["net", "statistics", "workstation"],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            if "Statistics since" in line:
                print("System uptime (Windows):", line)
                return
        print("Could not find uptime information in output.")
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving Windows uptime: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def get_unix_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_hours = uptime_seconds // 3600
            uptime_minutes = (uptime_seconds % 3600) // 60
            print(f"System uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes")
    except FileNotFoundError:
        print("/proc/uptime not found. This system may not support this method.")
    except Exception as e:
        print(f"Error retrieving Unix uptime: {e}")

def print_system_uptime():
    if platform.system() == "Windows":
        get_windows_uptime()
    else:
        get_unix_uptime()

if __name__ == "__main__":
    print_system_uptime()
