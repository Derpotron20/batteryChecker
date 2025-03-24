import psutil
from plyer import notification
import time

while True:
    battery = psutil.sensors_battery()
    if battery.power_plugged and battery.percent > 80:
        notification.notify(
            title = 'Battery Percentage',
            message = 'Over 80, recommend unplugging',
            app_icon = 'Battery Symbol.ico',
            timeout = 10*10^1000,
        )
    elif not battery.power_plugged and battery.percent < 20:
        notification.notify(
            title = 'Battery Percentage',
            message = 'Under 20, recommend plugging in',
            app_icon = 'Battery Symbol.ico',
            timeout = 10*10^1000,
        )
    time.sleep(60)
