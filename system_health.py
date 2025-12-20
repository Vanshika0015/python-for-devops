import psutil
def system_health():
    cpu=int(input("Enter the CPU percentage: "))
    disk=int(input("Enter disk usage of System: "))
    memory=int(input("Enter memory usage of system: "))

    sys_cpu=psutil.cpu_percent(interval=1)
    sys_disk=psutil.disk_usage("/").percent
    sys_memory=psutil.virtual_memory().percent

    print(f"Current CPU Usage: {sys_cpu}%")
    print(f"Current disk Usage: {sys_disk}%")
    print(f"Current memory Usage: {sys_memory}%")

    if sys_cpu > cpu:
        print("The current CPU usage is greater than threshold limit")
    else:
        print("The CPU usage is in control")
    if sys_disk>disk:
        print("The disk usgae is gretaer than threshold value")
    else:
        print("The disk usage is in control")
    if sys_memory>memory:
        print("The memoray usage is greater than threshold value")
    else:
        print("The disk usage is in control")
system_health()