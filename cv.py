import psutil
import platform
import GPUtil
import time
import numpy as np
import multiprocessing
import random
import math

# Function to simulate heavy CPU load
def cpu_task():
    while True:
        math.factorial(random.randint(10000, 20000))

def cpu_stress_test():
    print("Starting CPU stress test...")
    cpu_count = multiprocessing.cpu_count()
    processes = []
    for _ in range(cpu_count):
        p = multiprocessing.Process(target=cpu_task)
        p.start()
        processes.append(p)
    
    time.sleep(10)  # Run for 10 seconds then stop
    for p in processes:
        p.terminate()
    print("CPU stress test completed.")

# Function to check CPU & GPU details
def get_system_info():
    print("\nChecking system info...")
    system_info = {
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": round(psutil.virtual_memory().total / (1024 ** 3), 2)
    }
    
    print("System Info:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
    
    print("\nChecking GPU info...")
    gpus = GPUtil.getGPUs()
    if gpus:
        for gpu in gpus:
            print(f"GPU: {gpu.name}")
            print(f"Memory Total: {gpu.memoryTotal}MB")
            print(f"Memory Free: {gpu.memoryFree}MB")
            print(f"Memory Used: {gpu.memoryUsed}MB")
            print(f"GPU Load: {gpu.load * 100}%")
    else:
        print("No GPU detected!")

# Function to check battery health
def battery_health():
    print("\nChecking battery health...")
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery Percentage: {battery.percent}%")
        print("Charging" if battery.power_plugged else "Not Charging")
    else:
        print("Battery info not available.")

# Function to test laptop for heavy coding & app development
def performance_check():
    print("\nAnalyzing laptop performance...")
    if psutil.cpu_count(logical=True) >= 8 and psutil.virtual_memory().total / (1024 ** 3) >= 16:
        print("✅ This laptop is suitable for heavy coding!")
    else:
        print("⚠️ This laptop may struggle with heavy coding.")
    
    if GPUtil.getGPUs():
        print("✅ This laptop can handle app development tasks.")
    else:
        print("⚠️ This laptop may not be ideal for app development due to lack of GPU acceleration.")

if __name__ == "__main__":
    get_system_info()
    battery_health()
    performance_check()
    cpu_stress_test()
