from PySide6.QtWidgets import QMainWindow

from ui_SettingsDialog import Ui_Dialog

# TODO: implement window icon
# TODO: implement browsing for alarm sounds
# TODO: implement accept and discard actions

class SettingsDialog(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.setupUi(self)

    def accept(self):
        pass

    def reject(self):
        pass

    def set_low_alarm(self, text):
        self.edt_low_alarm.setText(text)

    def set_high_alarm(self, text):
        self.edt_high_alarm.setText(text)

    def set_check_interval(self, val):
        self.sl_check_interval.setValue(val)

    def set_min_percent(self, val):
        self.sl_min_percent.setValue(val)

    def set_max_percent(self, val):
        self.sl_max_percent.setValue(val)