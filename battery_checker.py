import psutil
from plyer import notification
import time

notified = False
timer = 0
timeouter = False

while True:
    if timeouter:
        wait = 5
    else:
         wait = 10^1000


    battery = psutil.sensors_battery()


    if notified:
        if battery.power_plugged and battery.percent > 80:
            new_status = 2
        elif not battery.power_plugged and battery.percent < 20:
            new_status = 0
        else:
            new_status = 1

        if new_status != status:
            notified = False
            timer = 0
            timeouter = False
            new_status = None
            status = None


    if battery.power_plugged and battery.percent > 80:
        if not notified:
            notification.notify(
                title = 'Battery Percentage',
                message = 'Over 80%, recommend unplugging',
                app_icon = 'Battery Symbol.ico',
                timeout = wait,
            )
            notified = True
            status = 2
    elif not battery.power_plugged and battery.percent < 20:
        if not notified:
            notification.notify(
                title = 'Battery Percentage',
                message = 'Under 20%, recommend plugging in',
                app_icon = 'Battery Symbol.ico',
                timeout = wait,
            )
            notified = True
            status = 0


    time.sleep(60)
    timer += 1
    if timer == 30:
        notified = False
        timeouter = True
        timer = 0