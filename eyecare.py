# import win10toast
from win10toast import ToastNotifier
import time
import keyboard as kb
# create bat file on windows
import getpass
import os

USER_NAME = getpass.getuser()

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "eyecare.bat", "w") as bat_file:
        bat_file.write(r'python %s\eyecare.py' % file_path)

add_to_startup()

# create an object to ToastNotifier class
n = ToastNotifier()
exit_key_not_pressed = True
while exit_key_not_pressed:
    n.show_toast("ALERT - EYE CARE", "GET YOUR EYES OFF OFF THE SCREEN FOR 1 MINUTE!!!!", duration=1800)
