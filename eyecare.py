# import win10toast
from win10toast import ToastNotifier
import time
import keyboard as kb
# create an object to ToastNotifier class
n = ToastNotifier()
exit_key_not_pressed = True
while exit_key_not_pressed:
    n.show_toast("ALERT - EYE CARE", "GET YOUR EYES OFF OFF THE SCREEN FOR 1 MINUTE!!!!", duration=1800)
