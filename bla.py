#!/usr/bin/env python3

# Based on: https://www.geeksforgeeks.org/create-battery-notifier-for-laptop-using-python/
# By abhisheksrivastaviot18

import psutil
from plyer import notification
from playsound import playsound
import time
import os

from debug import print_debug_message

# Debug flag
IS_DEBUGGING = True

# Default battery levels in percents
MIN_PERCENT = 15
MAX_PERCENT = 92

# Default check interval im minutes
CHECK_INTERVAL = 0.5 #3

# Sound files
SOUND_BATTERY_LOW = os.path.join('res', 'mixkit-alert-alarm-1005.wav')
SOUND_BATTERY_HIGH = os.path.join('res', 'alarm-no3-14864.mp3')

# Get battery data
battery = psutil.sensors_battery()

# Set previous percent to current battery level
prev_percent = battery.percent

# Try to detect if the device is plugged
is_charging = True if battery.power_plugged else False

# TODO: store settings in the settings file
# TODO: add tray icon and GUI for settings


def notify(text, sound_file):
	"""
	Shows tray notification and plays sound alarm
	:param text: text to display
	:param sound_file: sound alarm to play
	:return: None
	"""
	notification.notify(
		title="Battery Percentage",
		message=text,
		timeout=10
	)

	playsound(sound_file)


while True:
	# Refresh battery value each iteration
	battery = psutil.sensors_battery()

	# Get battery data into variables
	percent = battery.percent
	secs_left = battery.secsleft
	is_plugged = battery.power_plugged

	if IS_DEBUGGING:
		print_debug_message(percent, prev_percent, secs_left, is_plugged)

	# Notify user of low battery
	if percent < MIN_PERCENT and not is_plugged and not is_charging:
		message = f'''Battery percent ({percent}%) is below minimum ({MAX_PERCENT}%).
Please connect the power chord.'''
		notify(message, SOUND_BATTERY_LOW)

	# Notify user of high battery
	elif (percent > MAX_PERCENT or percent == 100) and is_plugged and is_charging:
		message = f'''Battery percent ({percent}%) exceeds maximum ({MAX_PERCENT}%).
Please disconnect the power chord.'''
		notify(message, SOUND_BATTERY_HIGH)
	
	# Check each CHECK_INTERVAL minutes
	time.sleep(60 * CHECK_INTERVAL)

