import psutil
from plyer import notification
import time

responded = False
timer = 0
timeout = False

while True:
    battery = psutil.sensors_battery()
    if not timeout:
        waittime = 10^1000
    else:
        waittime = 5
    if battery.power_plugged and battery.percent > 80:
        if not responded:
            notification.notify(
                title = 'Battery Percentage',
                message = 'Over 80, recommend unplugging',
                app_icon = 'Battery Symbol.ico',
                timeout = waittime,
            )
            responded = True
    elif not battery.power_plugged and battery.percent < 20:
        if not responded:
            notification.notify(
                title = 'Battery Percentage',
                message = 'Under 20, recommend plugging in',
                app_icon = 'Battery Symbol.ico',
                timeout = waittime,
            )
            responded = True
    time.sleep(60)
    timer += 1
    if timer == 30:
        responded = False
        timeout = True
