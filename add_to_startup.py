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
