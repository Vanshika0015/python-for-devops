# aapko kaam karna hai ki user se CPU threshold lo 
#current cpu usage pata karo
#agar cpu usage threshold se zayda hua, email kar do
import psutil
def cpu_threshold():
    user_cpu=int(input("Enter CPU threshold:" ))
    current_cpu= psutil.cpu_percent(interval=1)

    if current_cpu > user_cpu:
        print("CPU Alert Email sent...")
    else:
        print("CPU is in safe state")

cpu_threshold()