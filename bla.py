#!/usr/bin/python

# Declare localization functions at the top
from i18n import _, ngettext

import os, sys
import threading
from datetime import timedelta

import psutil
from playsound import playsound

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from const import *

from ui_SettingsDialog import Ui_Dialog
from debug import print_debug_message
from config import *

# TODO: Delete the following strings used for debugging purposes
# Debug flag
IS_DEBUGGING = True

APP_TITLE = _('Battery level Alert')

# TODO: Delete the following strings used for debugging purposes
# if IS_DEBUGGING:
#     CHECK_INTERVAL = 0.5
#     MIN_PERCENT = 53 # Alarm if < min
#     MAX_PERCENT = 55 # Alarm if > max


def get_tray_icon(percent, is_charging):
    if is_charging:
        image_name = 'battery-charge.png'
    else:
        if percent >= 95:
            image_name = 'battery-full.png'
        elif percent >= 20:
            image_name = 'battery--minus.png'
        elif percent > 5:
            image_name = 'battery-low.png'
        else:
            image_name = 'battery-empty.png'

    print(image_name)

    return os.path.join(ICONS_DIR, image_name)


def get_time_left_str(secs_left):
    if secs_left == psutil.POWER_TIME_UNKNOWN:
        time_left_str = _('unknown')
    elif secs_left == psutil.POWER_TIME_UNLIMITED:
        time_left_str = _('unlimited')
    else:
        time_left_str = str(timedelta(seconds=secs_left))[:-3]
    return time_left_str


class App:
    def __init__(self):
        # Create a Qt application
        self.app = QApplication(sys.argv)
        # Prevent app from exiting when the window is closed
        self.app.setQuitOnLastWindowClosed(False)

        # Create a settings dialog
        self.dialog = Ui_Dialog()

        # Create menu
        menu = QMenu()
        self.settings_action = menu.addAction(_("Settings"))
        self.settings_action.triggered.connect(self.setting)
        self.exit_action = menu.addAction(_("Exit"))
        self.exit_action.triggered.connect(sys.exit)

        # Get initial battery data
        self.battery = psutil.sensors_battery()
        # Store current percent to detect the state
        self.prev_percent = self.battery.percent

        # Create tray icon
        self.tray = QSystemTrayIcon()

        is_plugged = True if self.battery.power_plugged else False
        self.tray.setIcon(QIcon(get_tray_icon(self.battery.percent, is_plugged)))
        self.tray.setContextMenu(menu)
        self.tray.setToolTip(f'{_("Time left:")} {get_time_left_str(self.battery.secsleft)} ({self.battery.percent} %)')

        self.tray.show()

        # Run initial check
        self.check_battery()

        # Create and start timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_battery)
        self.timer.start(int(CHECK_INTERVAL * 60 * 1000))

    def check_battery(self):
        # Check current data
        self.battery = psutil.sensors_battery()
        percent = self.battery.percent
        is_plugged = True if self.battery.power_plugged else False
        self.tray.setIcon(QIcon(get_tray_icon(percent, is_plugged)))

        if IS_DEBUGGING:
            print_debug_message(percent, self.prev_percent, self.battery.secsleft, is_plugged)

        # Set tray tooltip
        self.tray.setToolTip(f'{_("Time left:")} {get_time_left_str(self.battery.secsleft)} ({self.battery.percent} %)')

        # Check for low or high battery
        is_charging = self.battery.power_plugged or percent > self.prev_percent

        # Notify user of low battery
        if percent < MIN_PERCENT and not is_plugged and not is_charging:
            message = f'''{_("Battery percent")} ({percent}%) {_("is below minimum")} ({MAX_PERCENT}%).
    {_("Please connect the power chord.")}'''
            self.notify(APP_TITLE, message, SOUND_BATTERY_LOW)

        # Notify user of high battery
        elif (percent > MAX_PERCENT or percent == 100) and is_plugged and is_charging:
            message = f'''{_("Battery percent")} ({percent}%) {_("exceeds maximum")} ({MAX_PERCENT}%).
    {_("Please disconnect the power chord.")}'''
            self.notify(APP_TITLE, message, SOUND_BATTERY_HIGH)

        # Update previous percent with current data
        self.prev_percent = percent

    def run(self):
        # Enter Qt application main loop
        self.app.exec()
        sys.exit()

    def setting(self):
        self.dialog.set_check_interval(CHECK_INTERVAL)
        self.dialog.set_min_percent(MIN_PERCENT)
        self.dialog.set_max_percent(MAX_PERCENT)
        self.dialog.set_low_alarm(SOUND_BATTERY_LOW)
        self.dialog.set_high_alarm(SOUND_BATTERY_HIGH)
        self.dialog.retranslateUi()
        self.dialog.show()

    def notify(self, title, text, sound):
        # Notify user of battery level
        self.tray.showMessage(title, text)
        # Play sound in a separate thread (daemon)
        sound_thread = threading.Thread(target=playsound, args=(sound,))
        sound_thread.daemon = True
        sound_thread.start()


if __name__ == "__main__":
    app = App()
    app.run()
