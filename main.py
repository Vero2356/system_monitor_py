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
print(f"Boot Time: {bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")

# printing information about CPU like cores, threads, freq., etc.

print("="*40, "CPU Info", "="*40)
# cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

# frequency
cpufreq = psutil.cpu_freq()
print(f"Max frequency {cpufreq.max:.02f}Mhz")
print(f"Min frequency {cpufreq.min:.02f}Mhz")
print(f"current frequency {cpufreq.current:.02f}Mhz")

# usage
print("CPU Usage per Core")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
