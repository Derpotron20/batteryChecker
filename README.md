# Battery Checker
## Purpose
To preserve battery life as long as possible by keeping your laptop between 20-80% charged, through notifying the user of when to charge and when to stop charging.
## What it does
Will check the users battery percentage, and if the user is charging. If charging and over 80% charged, will notify the user to unplug, and if not charging and under 20% will notify to plug in. After first notification will wait 30 mins before sending a second one. If the status changes at all (any combination of the previously stated variables), then the timer will reset and if will then notify you the next time the computer fits the variables.

If full 30 mins ticks over without change, then user will be notified again, but instead of the notification lingering around until you click it, it will only stay 5 secs in case user purposely ignored  the notification. Will then repeat cycle over and over again.

## Dependecies
To use will require:
Python, and inside it:
1. time (pre-installed) (for waiting between checks)
2. psutil (for access to battery data)
3. plyer (for ability to use notifications)
