import psutil
from plyer import notification
from playsound import playsound
import math

battery = psutil.sensors_battery()
percent = battery.percent

notification.notify(
		title="Battery Percentage",
		message=str(math.floor(percent)) + " % battery",
		timeout=10
	)
playsound('Alarm from Assignment - Earth.mp3')