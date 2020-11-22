# import win10toast
from win10toast import ToastNotifier
import time

# create an object to ToastNotifier class
n = ToastNotifier()
exit_key_not_pressed = True
while exit_key_not_pressed:
    n.show_toast("ALERT - EYE CARE", "GET YOUR EYES OFF OFF THE SCREEN FOR 1 MINUTE!!!! Look at an object 20 feet away", duration=1200)
