# importing libraries
import platform
import psutil
from datetime import datetime
import time
import os

# Function for converting large number to readeable ones for normal people
def convert_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def clear_screen():
    # Use 'cls' for Windows, 'clear' for others
    os.system('cls' if os.name == 'nt' else 'clear')

# Get update interval from user
Time = int(input("Enter the amount of seconds before reloading data: "))

try:
    # Main loop for continuous monitoring
    while True:
        clear_screen()

        print("="*40, "System Information", "="*40)
        
        # System info needs to be reprinted after clear
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
        if cpufreq:
            print(f"Max frequency {cpufreq.max:.02f}Mhz")
            print(f"Min frequency {cpufreq.min:.02f}Mhz")
            print(f"current frequency {cpufreq.current:.02f}Mhz")

        # usage
        print("CPU Usage per Core:")
        # Measures CPU over 1 sec interval
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

        # Memory information
        print("="*40, "Memory Information", "="*40)

        svmem = psutil.virtual_memory()
        print(f"Total: {convert_size(svmem.total)}")
        print(f"Avaible: {convert_size(svmem.available)}")
        print(f"Used: {convert_size(svmem.used)}")
        print(f"Percentage:{svmem.percent}%")
        
        print("="*20, "SWAP", "="*20)

        # Swap memory
        swap = psutil.swap_memory()
        print(f"Total: {convert_size(swap.total)}")
        print(f"Free: {convert_size(swap.free)}")
        print(f"Used: {convert_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

        # Disk usage
        print("="*40, "Disk Information", "="*40)

        print("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {convert_size(partition_usage.total)}")
            print(f"  Used: {convert_size(partition_usage.used)}")
            print(f"  Free: {convert_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")

        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {convert_size(disk_io.read_bytes)}")
        print(f"Total write: {convert_size(disk_io.write_bytes)}")
        
        print("\n" + "="*80)
        print("Press Ctrl+C to exit")

        # Wait user-defined seconds before reload
        time.sleep(Time)

# Handle clean exit on Ctrl+C
except KeyboardInterrupt:
    print("\n")
    print("="*40)
    print("Program stopped by user. Goodbye!")
    print("="*40)