#!/usr/bin/env python3

# Source: https://www.geeksforgeeks.org/create-battery-notifier-for-laptop-using-python/
# Author abhisheksrivastaviot18

import psutil
from plyer import notification
from playsound import playsound
import time
import math

MIN_PERCENT = 15
MAX_PERCENT = 92
SOUND = 'Alarm from Assignment - Earth.mp3'
# TODO: add sound for low/high battery
CHECK_INTERVAL = 3

# TODO: store settings in the settings file
#TODO: add tray icon and GUI for settings

def notify(text, sound_file):
	notification.notify(
		title="Battery Percentage",
		message=text,
		timeout=10
	)

	playsound(sound_file)

while True:
	battery = psutil.sensors_battery()
	percent = battery.percent

	if percent <= MIN_PERCENT:
		message = f'{math.floor(percent)}% battery remaining'
		notify(message, SOUND)
	
	elif percent >= MAX_PERCENT:
		message = f'{math.floor(percent)}% battery reached'
		notify(message, SOUND)

	#TODO: Repeat alert if battery:
	# continues to discharge under MIN_PERCENT
	# continues to charge over MAX_PERCENT or stays at 100%
	
	# Check each CHECK_INTERVAL minutes
	time.sleep(60*CHECK_INTERVAL)
	
	continue

