# -*- coding: utf-8 -*-

from PySide6.QtCore import (QMetaObject, Qt)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QDialogButtonBox,
                               QGridLayout, QLabel, QLineEdit, QPushButton,
                               QSpinBox, QWidget, QFileDialog, QMainWindow)

from config import *
from i18n import _


# TODO: implement locale selection and get info about packaging for different platforms
# TODO: implement GUI icon

class Ui_Dialog(QMainWindow):
    def __init__(self):
        super().__init__()

        if not self.objectName():
            self.setObjectName(u"Dialog")
        self.resize(586, 300)
        self.setWindowIcon(QIcon(os.path.join(ICONS_DIR, 'battery--pencil.png')))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")

        self.label_check_interval = QLabel(self)
        self.label_check_interval.setObjectName(u"label_check_interval")

        self.gridLayout.addWidget(self.label_check_interval, 0, 0)

        self.sp_check_interval = QSpinBox(self)
        self.sp_check_interval.setObjectName(u"sp_check_interval")
        self.sp_check_interval.setMaximum(60)
        self.sp_check_interval.setMinimum(1)
        self.sp_check_interval.setValue(3)

        self.gridLayout.addWidget(self.sp_check_interval, 0, 1)

        self.edt_low_alarm = QLineEdit(self)
        self.edt_low_alarm.setObjectName(u"edt_low_alarm")

        self.gridLayout.addWidget(self.edt_low_alarm, 3, 1)

        self.label_high_alarm = QLabel(self)
        self.label_high_alarm.setObjectName(u"label_high_alarm")

        self.gridLayout.addWidget(self.label_high_alarm, 4, 0)

        self.sp_max_percent = QSpinBox(self)
        self.sp_max_percent.setObjectName(u"sp_max_percent")
        self.sp_max_percent.setMinimum(70)
        self.sp_max_percent.setMaximum(100)
        self.sp_max_percent.setValue(80)

        self.gridLayout.addWidget(self.sp_max_percent, 2, 1)

        self.label_max_percent = QLabel(self)
        self.label_max_percent.setObjectName(u"label_max_percent")

        self.gridLayout.addWidget(self.label_max_percent, 2, 0)

        self.edt_high_alarm = QLineEdit(self)
        self.edt_high_alarm.setObjectName(u"edt_high_alarm")

        self.gridLayout.addWidget(self.edt_high_alarm, 4, 1)

        self.label_min_percent = QLabel(self)
        self.label_min_percent.setObjectName(u"label_min_percent")

        self.gridLayout.addWidget(self.label_min_percent, 1, 0)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        # TODO: Localize buttonBox
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0)

        self.sp_min_percent = QSpinBox(self)
        self.sp_min_percent.setObjectName(u"sp_min_percent")
        self.sp_min_percent.setMaximum(30)
        self.sp_min_percent.setMinimum(0)
        self.sp_min_percent.setValue(20)

        self.gridLayout.addWidget(self.sp_min_percent, 1, 1)

        self.label_low_alarm = QLabel(self)
        self.label_low_alarm.setObjectName(u"label_low_alarm")

        self.gridLayout.addWidget(self.label_low_alarm, 3, 0)

        self.btn_browse_low_alarm = QPushButton(self)
        self.btn_browse_low_alarm.setObjectName(u"btn_browse_low_alarm")

        self.gridLayout.addWidget(self.btn_browse_low_alarm, 3, 2)

        self.btn_browse_high_alarm = QPushButton(self)
        self.btn_browse_high_alarm.setObjectName(u"btn_browse_high_alarm")

        self.gridLayout.addWidget(self.btn_browse_high_alarm, 4, 2)

        self.widget = QWidget()
        self.widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.widget)

        # Connect events to handlers

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.btn_browse_high_alarm.clicked.connect(self.get_high_alarm)
        self.btn_browse_low_alarm.clicked.connect(self.get_low_alarm)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def accept(self):
        config['DEFAULT'] = {
            'SOUND_BATTERY_LOW': self.edt_low_alarm.text(),
            'SOUND_BATTERY_HIGH': self.edt_high_alarm.text(),
            'CHECK_INTERVAL': self.sp_check_interval.value(),
            'MIN_PERCENT': self.sp_min_percent.value(),
            'MAX_PERCENT': self.sp_max_percent.value()
        }
        config_apply(config)
        config_write(config)
        self.hide()

    def reject(self):
        self.hide()

    def set_low_alarm(self, text):
        self.edt_low_alarm.setText(text)

    def set_high_alarm(self, text):
        self.edt_high_alarm.setText(text)

    def set_check_interval(self, val):
        self.sp_check_interval.setValue(val)

    def set_min_percent(self, val):
        self.sp_min_percent.setValue(val)

    def set_max_percent(self, val):
        self.sp_max_percent.setValue(val)

    def get_high_alarm(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        dlg.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        set_filter = _('Sound files (*.wav *.mp3)')
        result = dlg.getOpenFileName(self,
                                     _('Battery high alarm'),
                                     SOUNDS_DIR,
                                     'Sound files (*.wav *.mp3);;All files (*.*)',
                                     set_filter)
        if (result[0]):
            self.edt_low_alarm.setText(result[0])

    def get_low_alarm(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        dlg.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        set_filter = _('Sound files (*.wav *.mp3)')
        result = dlg.getOpenFileName(self,
                                     _('Battery low alarm'),
                                     SOUNDS_DIR,
                                     'Sound files (*.wav *.mp3);;All files (*.*)',
                                     set_filter)
        if result[0]:
            self.edt_low_alarm.setText(result[0])

    def retranslateUi(self):
        self.setWindowTitle(_("Settings"))
        self.label_high_alarm.setText(_("Battery high alarm"))
        self.label_check_interval.setText(_("Check interval, minutes"))
        self.label_max_percent.setText(_("Max. battery percent, 70%–100%"))
        self.label_min_percent.setText(_("Min. battery percent, 0%–30%"))
        self.label_low_alarm.setText(_("Battery low alarm"))
        self.btn_browse_low_alarm.setText(_("..."))
        self.btn_browse_high_alarm.setText(_("..."))
    # retranslateUi
