Copilot Test
This project explores my experience using GitHub Copilot to generate a Python script that displays the system uptime across Windows and Unix systems.

What code did Copilot generate?
I prompted Copilot to write a script that would print the system uptime for both Windows and Unix platforms. The generated code included:

Functions to fetch uptime for Windows (parsing net statistics workstation output) and Unix-like systems (reading /proc/uptime)
A platform check to choose the appropriate function
Error handling for common issues
Here is the main structure Copilot produced:

Python
import platform
import subprocess

def get_windows_uptime():
    # ...

def get_unix_uptime():
    # ...

def print_system_uptime():
    # ...

if __name__ == "__main__":
    print_system_uptime()
Did I modify the script?
Yes. I reviewed the code Copilot generated and made sure:

The output messages were clear and user-friendly.
Exceptions were handled gracefully, especially for systems where uptime is not available.
The script works for both Windows and Unix-like systems (Linux, macOS).
How did I test it?
I tested the script on both a Windows machine and a Linux system:

On Windows, it fetches system uptime using the net statistics workstation command.
On Linux, it reads from /proc/uptime.
I verified that the script prints the correct uptime or an appropriate error message.
How to run the script
Make sure you have Python 3 installed.
Download copilot_test.py from this repository.
Open a terminal or command prompt and navigate to the folder containing copilot_test.py.
Run the script with:
bash
python copilot_test.py
On Windows, it will display the uptime since last boot using system commands.
On Unix-like systems (Linux, macOS), it will read and display uptime from /proc/uptime.
