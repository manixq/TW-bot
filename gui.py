# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike\Desktop\Villentretenmerth\Selenium\tribal wars bot\tw.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setWindowTitle(_fromUtf8("TW bot"))
        Dialog.setToolTip(_fromUtf8(""))
        Dialog.setStatusTip(_fromUtf8(""))
        Dialog.setWhatsThis(_fromUtf8(""))
        self.spear_box = QtGui.QSpinBox(Dialog)
        self.spear_box.setGeometry(QtCore.QRect(130, 70, 42, 22))
        self.spear_box.setObjectName(_fromUtf8("spear_box"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 50, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.sword_box = QtGui.QSpinBox(Dialog)
        self.sword_box.setGeometry(QtCore.QRect(180, 70, 42, 22))
        self.sword_box.setObjectName(_fromUtf8("sword_box"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.axe_box = QtGui.QSpinBox(Dialog)
        self.axe_box.setGeometry(QtCore.QRect(230, 70, 42, 22))
        self.axe_box.setObjectName(_fromUtf8("axe_box"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 50, 41, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.light_box = QtGui.QSpinBox(Dialog)
        self.light_box.setGeometry(QtCore.QRect(280, 70, 42, 22))
        self.light_box.setObjectName(_fromUtf8("light_box"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 41, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.scout_box = QtGui.QSpinBox(Dialog)
        self.scout_box.setGeometry(QtCore.QRect(330, 70, 42, 22))
        self.scout_box.setObjectName(_fromUtf8("scout_box"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(330, 50, 41, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ram_box = QtGui.QSpinBox(Dialog)
        self.ram_box.setGeometry(QtCore.QRect(380, 70, 42, 22))
        self.ram_box.setObjectName(_fromUtf8("ram_box"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(380, 50, 41, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cata_box = QtGui.QSpinBox(Dialog)
        self.cata_box.setGeometry(QtCore.QRect(430, 70, 42, 22))
        self.cata_box.setObjectName(_fromUtf8("cata_box"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(430, 50, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.snob_box = QtGui.QSpinBox(Dialog)
        self.snob_box.setGeometry(QtCore.QRect(480, 70, 42, 22))
        self.snob_box.setObjectName(_fromUtf8("snob_box"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(480, 50, 41, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.progress_bar = QtGui.QProgressBar(Dialog)
        self.progress_bar.setGeometry(QtCore.QRect(130, 20, 391, 23))
        self.progress_bar.setProperty("value", 100)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.log_edit = QtGui.QPlainTextEdit(Dialog)
        self.log_edit.setGeometry(QtCore.QRect(130, 120, 391, 201))
        self.log_edit.setObjectName(_fromUtf8("log_edit"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(130, 100, 47, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.go_farm_button = QtGui.QPushButton(Dialog)
        self.go_farm_button.setGeometry(QtCore.QRect(130, 430, 141, 23))
        self.go_farm_button.setObjectName(_fromUtf8("go_farm_button"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(130, 350, 71, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.max_range_edit = QtGui.QLineEdit(Dialog)
        self.max_range_edit.setGeometry(QtCore.QRect(210, 350, 61, 20))
        self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.max_range_edit.setObjectName(_fromUtf8("max_range_edit"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(220, 330, 61, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(130, 400, 71, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(210, 380, 81, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.wait_time_edit = QtGui.QLineEdit(Dialog)
        self.wait_time_edit.setGeometry(QtCore.QRect(210, 400, 61, 20))
        self.wait_time_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.wait_time_edit.setObjectName(_fromUtf8("wait_time_edit"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(460, 330, 61, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.attack_at_edit = QtGui.QLineEdit(Dialog)
        self.attack_at_edit.setGeometry(QtCore.QRect(460, 350, 61, 20))
        self.attack_at_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.attack_at_edit.setObjectName(_fromUtf8("attack_at_edit"))
        self.attack_button = QtGui.QPushButton(Dialog)
        self.attack_button.setGeometry(QtCore.QRect(390, 430, 131, 23))
        self.attack_button.setObjectName(_fromUtf8("attack_button"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(390, 350, 71, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.world_edit = QtGui.QLineEdit(Dialog)
        self.world_edit.setGeometry(QtCore.QRect(0, 20, 91, 20))
        self.world_edit.setObjectName(_fromUtf8("world_edit"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 71, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.viewer = QtGui.QComboBox(Dialog)
        self.viewer.setGeometry(QtCore.QRect(0, 50, 91, 21))
        self.viewer.setObjectName(_fromUtf8("viewer"))
        self.viewer.addItem(_fromUtf8(""))
        self.viewer.addItem(_fromUtf8(""))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(460, 380, 61, 20))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.attack_on_edit = QtGui.QLineEdit(Dialog)
        self.attack_on_edit.setGeometry(QtCore.QRect(460, 400, 61, 20))
        self.attack_on_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.attack_on_edit.setObjectName(_fromUtf8("attack_on_edit"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(390, 400, 71, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.villages_box = QtGui.QSpinBox(Dialog)
        self.villages_box.setGeometry(QtCore.QRect(0, 110, 42, 22))
        self.villages_box.setObjectName(_fromUtf8("villages_box"))
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(0, 90, 61, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.label.setText(_translate("Dialog", "spear", None))
        self.label_2.setText(_translate("Dialog", "sword", None))
        self.label_3.setText(_translate("Dialog", "axe", None))
        self.label_4.setText(_translate("Dialog", "light", None))
        self.label_5.setText(_translate("Dialog", "scout", None))
        self.label_6.setText(_translate("Dialog", "ram", None))
        self.label_7.setText(_translate("Dialog", "cata", None))
        self.label_8.setText(_translate("Dialog", "snob", None))
        self.label_9.setText(_translate("Dialog", "Logs:", None))
        self.go_farm_button.setText(_translate("Dialog", "Go farm", None))
        self.label_10.setText(_translate("Dialog", "Max range:", None))
        self.max_range_edit.setText(_translate("Dialog", "2:30", None))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">[hh:mm]</span></p></body></html>", None))
        self.label_12.setText(_translate("Dialog", "Wait time:", None))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">[min:max]</span><span style=\" font-size:10pt; vertical-align:super;\">sec</span></p></body></html>", None))
        self.wait_time_edit.setText(_translate("Dialog", "160:624", None))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">[hh:mm:ss]</span></p></body></html>", None))
        self.attack_at_edit.setText(_translate("Dialog", "7:00:00", None))
        self.attack_button.setText(_translate("Dialog", "Attack", None))
        self.label_15.setText(_translate("Dialog", "Attack at:", None))
        self.world_edit.setText(_translate("Dialog", "pl115", None))
        self.label_16.setText(_translate("Dialog", "World:", None))
        self.viewer.setItemText(0, _translate("Dialog", "Chrome", None))
        self.viewer.setItemText(1, _translate("Dialog", "Firefox", None))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">[x|y]</span></p></body></html>", None))
        self.attack_on_edit.setText(_translate("Dialog", "000|000", None))
        self.label_18.setText(_translate("Dialog", "Attack on:", None))
        self.label_19.setText(_translate("Dialog", "Villages", None))
