#!/usr/bin/python

import os, sys
from datetime import timedelta

import configparser

import psutil
from playsound import playsound

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from ui_SettingsDialog import Ui_Dialog
from debug import print_debug_message

# TODO: Delete the following strings used for debugging purposes
# Debug flag
IS_DEBUGGING = True

APP_TITLE = 'Battery Level Alert'

# Read or create configuration
config_file_name = 'settings.ini'
config = configparser.ConfigParser()

if not os.path.exists('settings.ini'):
    config['DEFAULT'] = {
        'SOUND_BATTERY_LOW': os.path.join('res', 'mixkit-alert-alarm-1005.wav'),
        'SOUND_BATTERY_HIGH': os.path.join('res', 'alarm-no3-14864.mp3'),
        'CHECK_INTERVAL': '3',
        'MIN_PERCENT': '15',
        'MAX_PERCENT': '95'
    }
    with open(config_file_name, 'w') as config_file:
        config.write(config_file)

config.read(config_file_name)


# Sound files
SOUND_BATTERY_LOW = config['DEFAULT']['SOUND_BATTERY_LOW']
SOUND_BATTERY_HIGH = config['DEFAULT']['SOUND_BATTERY_HIGH']

# Default battery levels in percents
MIN_PERCENT = int(config['DEFAULT']['MIN_PERCENT'])
MAX_PERCENT = int(config['DEFAULT']['MAX_PERCENT'])

# Default check interval im minutes
CHECK_INTERVAL = int(config['DEFAULT']['CHECK_INTERVAL'])

# TODO: Delete the following strings used for debugging purposes
if IS_DEBUGGING:
    CHECK_INTERVAL = 0.3


def get_tray_icon(level, is_charging):
    if is_charging and level >= 95:
        image_name = 'battery--exclamation.png'
    else:
        if level < 5:
            image_name = 'battery-empty.png'
        elif level >= 5 and level <= 20:
            image_name = 'battery-low.png'
        elif level > 20 and level <= 80:
            image_name = 'battery--minus.png'
        elif level > 80 and level <= 95:
            image_name = 'battery-full.png'
        else:
            image_name = 'battery--exclamation.png'

    return image_name


def get_time_left_str(secs_left):
    if secs_left == psutil.POWER_TIME_UNKNOWN:
        time_left_str = 'unknown'
    elif secs_left == psutil.POWER_TIME_UNLIMITED:
        time_left_str = 'unlimited'
    else:
        time_left_str = str(timedelta(seconds=secs_left))
    return time_left_str


class SettingsDialog(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def accept(self):
        pass

    def reject(self):
        pass

class App:
    def __init__(self):
        # Create a Qt application
        self.app = QApplication(sys.argv)
        # Prevent app from exiting when the window is closed
        self.app.setQuitOnLastWindowClosed(False)

        # Create a settings dialog
        self.dialog = SettingsDialog()

        # Create menu
        menu = QMenu()
        settingAction = menu.addAction("Settings")
        settingAction.triggered.connect(self.setting)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(sys.exit)

        # Create and start timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_battery)
        self.timer.start(int(CHECK_INTERVAL * 3600))

        # Get initial battery data
        self.battery = psutil.sensors_battery()
        # Store current percent to detect the state
        self.prev_percent = self.battery.percent

        # Create tray icon
        icon = QIcon(os.path.join('res', 'icons', 'battery-full.png'))
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.setToolTip(f'Time left: {get_time_left_str(self.battery.secsleft)} ({self.battery.percent} %)')
        self.tray.show()

    def check_battery(self):
        # Check current data
        self.battery = psutil.sensors_battery()
        percent = self.battery.percent
        is_plugged = True if self.battery.power_plugged else False
        self.tray.setIcon(QIcon(os.path.join('res', 'icons', get_tray_icon(percent, is_plugged))))

        if IS_DEBUGGING:
            print_debug_message(percent, self.prev_percent, self.battery.secsleft, is_plugged)

        # Set tray tooltip
        self.tray.setToolTip(f'Time left: {get_time_left_str(self.battery.secsleft)} ({self.battery.percent} %)')

        # Check for low or high battery
        is_charging = self.battery.power_plugged or percent > self.prev_percent

        # Notify user of low battery
        if percent < MIN_PERCENT and not is_plugged and not is_charging:
            message = f'''Battery percent ({percent}%) is below minimum ({MAX_PERCENT}%).
    Please connect the power chord.'''
            self.notify(APP_TITLE, message, SOUND_BATTERY_LOW)

        # Notify user of high battery
        elif (percent > MAX_PERCENT or percent == 100) and is_plugged and is_charging:
            message = f'''Battery percent ({percent}%) exceeds maximum ({MAX_PERCENT}%).
    Please disconnect the power chord.'''
            self.notify(APP_TITLE, message, SOUND_BATTERY_HIGH)

        # Update previous percent with current data
        self.prev_percent = percent

    def run(self):
        # Enter Qt application main loop
        self.app.exec()
        sys.exit()

    # TODO: Create GUI for settings
    # sound_battery_low = res\mixkit-alert-alarm-1005.wav
    # sound_battery_high = res\alarm-no3-14864.mp3
    # check_interval = 3
    # min_percent = 15
    # max_percent = 95
    def setting(self):
        self.dialog.setWindowTitle("Settings")
        self.dialog.show()

    def notify(self, title, text, sound):
        self.tray.showMessage(title, text)
        playsound(sound)


if __name__ == "__main__":
    app = App()
    app.run()
