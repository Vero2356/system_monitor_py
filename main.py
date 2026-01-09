# importing libraries
import platform
import psutil
from datetime import datetime

# Function for converting large number to readeable ones for normal people

def convert_size(bytes, suffix="B"):

    factor = 1024
    
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("="*40, "System Information", "="*40)

uname = platform.uname()

print(f"System: {uname.system}") # name of OS
print(f"Node name: {uname.node}") # name of notebook
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"CPU: {uname.processor}")

print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")