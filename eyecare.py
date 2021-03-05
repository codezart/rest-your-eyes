# import win10toast
from win10toast import ToastNotifier
import time, os
import wmi
c = wmi.WMI()

high_priority_processes = ["GenshinImpact.exe"]
# create an object to ToastNotifier class
n = ToastNotifier()
exit_key_not_pressed = True
while exit_key_not_pressed:
    n.show_toast("ALERT - EYE CARE", "GET YOUR EYES OFF OFF THE SCREEN FOR 1 MINUTE!!!! you will be locked out", duration=1200)
    time.sleep(10)
    running_Processes = list()
    for process in c.Win32_Process():
        running_Processes.append(process.Name)

    check = any(item in high_priority_processes for item in running_Processes)

    if check is False:
        os.system("rundll32.exe user32.dll,LockWorkStation")
    
