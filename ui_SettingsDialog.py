# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialogIZyCrp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSlider, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(586, 300)
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")

        self.edt_low_alarm = QLineEdit(Dialog)
        self.edt_low_alarm.setObjectName(u"edt_low_alarm")
        self.edt_low_alarm.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.edt_low_alarm, 3, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.label_5, 4, 0)

        self.sl_check_interval = QSlider(Dialog)
        self.sl_check_interval.setObjectName(u"sl_check_interval")
        self.sl_check_interval.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.sl_check_interval.setMaximum(60)
        self.sl_check_interval.setValue(3)
        self.sl_check_interval.setOrientation(Qt.Horizontal)
        self.sl_check_interval.setTickPosition(QSlider.TicksAbove)
        self.sl_check_interval.setTickInterval(1)

        self.gridLayout.addWidget(self.sl_check_interval, 0, 1)

        self.label_check_interval = QLabel(Dialog)
        self.label_check_interval.setObjectName(u"label_check_interval")
        self.label_check_interval.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.label_check_interval, 0, 0)

        self.sl_max_level = QSlider(Dialog)
        self.sl_max_level.setObjectName(u"sl_max_level")
        self.sl_max_level.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.sl_max_level.setMinimum(70)
        self.sl_max_level.setMaximum(100)
        self.sl_max_level.setValue(80)
        self.sl_max_level.setOrientation(Qt.Horizontal)
        self.sl_max_level.setTickPosition(QSlider.TicksAbove)
        self.sl_max_level.setTickInterval(1)

        self.gridLayout.addWidget(self.sl_max_level, 2, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.label_3, 2, 0)

        self.edt_full_alarm = QLineEdit(Dialog)
        self.edt_full_alarm.setObjectName(u"edt_full_alarm")
        self.edt_full_alarm.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.edt_full_alarm, 4, 1)

        self.label_min_level = QLabel(Dialog)
        self.label_min_level.setObjectName(u"label_min_level")
        self.label_min_level.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.label_min_level, 1, 0)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0)

        self.sl_min_level = QSlider(Dialog)
        self.sl_min_level.setObjectName(u"sl_min_level")
        self.sl_min_level.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.sl_min_level.setMaximum(30)
        self.sl_min_level.setValue(20)
        self.sl_min_level.setOrientation(Qt.Horizontal)
        self.sl_min_level.setTickPosition(QSlider.TicksAbove)
        self.sl_min_level.setTickInterval(1)

        self.gridLayout.addWidget(self.sl_min_level, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.label_4, 3, 0)

        self.btn_browse_low_alarm = QPushButton(Dialog)
        self.btn_browse_low_alarm.setObjectName(u"btn_browse_low_alarm")
        self.btn_browse_low_alarm.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.btn_browse_low_alarm, 3, 2)

        self.btn_browse_full_alarm = QPushButton(Dialog)
        self.btn_browse_full_alarm.setObjectName(u"btn_browse_full_alarm")
        self.btn_browse_full_alarm.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.btn_browse_full_alarm, 4, 2)

        self.label_check_interval_value = QLabel(Dialog)
        self.label_check_interval_value.setObjectName(u"label_check_interval_value")

        self.gridLayout.addWidget(self.label_check_interval_value, 0, 2)

        self.label_min_level_value = QLabel(Dialog)
        self.label_min_level_value.setObjectName(u"label_min_level_value")

        self.gridLayout.addWidget(self.label_min_level_value, 1, 2)

        self.label_max_level_value = QLabel(Dialog)
        self.label_max_level_value.setObjectName(u"label_max_level_value")

        self.gridLayout.addWidget(self.label_max_level_value, 2, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.sl_check_interval.valueChanged.connect(self.label_check_interval_value.setNum)
        self.sl_min_level.valueChanged.connect(self.label_min_level_value.setNum)
        self.sl_max_level.valueChanged.connect(self.label_max_level_value.setNum)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Batery full alarm", None))
        self.label_check_interval.setText(QCoreApplication.translate("Dialog", u"Check interval, min", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Max. battery level, 70%\u2013100%", None))
        self.label_min_level.setText(QCoreApplication.translate("Dialog", u"Min. battery level, 0%\u201330%", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Batery low alarm", None))
        self.btn_browse_low_alarm.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.btn_browse_full_alarm.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_check_interval_value.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.label_min_level_value.setText(QCoreApplication.translate("Dialog", u"20%", None))
        self.label_max_level_value.setText(QCoreApplication.translate("Dialog", u"80%", None))
    # retranslateUi

