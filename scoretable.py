# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sct.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class Init_UI(object):

    def __init__(self):
        self.tableView = QtWidgets.QTableView(Dialog)
        self.spButton = QtWidgets.QCheckBox(Dialog)
        self.dpButton = QtWidgets.QCheckBox(Dialog)
        self.level11Button = QtWidgets.QCheckBox(Dialog)
        self.level12Button = QtWidgets.QCheckBox(Dialog)
        self.getfileButton = QtWidgets.QToolButton(Dialog)
        self.fileoutButton = QtWidgets.QPushButton(Dialog)
        self.introductionButton = QtWidgets.QPushButton(Dialog)
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.filenamelabel = QtWidgets.QLabel(Dialog)
        self.titlelabel = QtWidgets.QLabel(Dialog)
        self.dialog = Dialog
        self.setupUi(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 768)
        Dialog.setMinimumSize(QtCore.QSize(1024, 768))
        Dialog.setMaximumSize(QtCore.QSize(1024, 768))
        self.titlelabel.setGeometry(QtCore.QRect(9, 9, 195, 16))
        self.titlelabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titlelabel.setObjectName("titlelabel")  # 타이틀
        self.filenamelabel.setGeometry(QtCore.QRect(9, 300, 195, 16))
        self.filenamelabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.filenamelabel.setObjectName("filenamelabel")  # 파일 이름
        self.tableView.setGeometry(QtCore.QRect(100, 30, 911, 721))
        self.tableView.setObjectName("tableView")  # 테이블
        self.spButton.setGeometry(QtCore.QRect(10, 34, 68, 16))
        self.spButton.setMaximumSize(QtCore.QSize(90, 16))
        self.spButton.setObjectName("spButton")  # SP select
        self.dpButton.setGeometry(QtCore.QRect(10, 56, 68, 16))
        self.dpButton.setMaximumSize(QtCore.QSize(90, 16))
        self.dpButton.setObjectName("dpButton")  # DP select
        self.level11Button.setGeometry(QtCore.QRect(10, 78, 69, 16))
        self.level11Button.setMaximumSize(QtCore.QSize(90, 16))
        self.level11Button.setObjectName("level11Button")  # level 11 select
        self.level12Button.setGeometry(QtCore.QRect(10, 100, 69, 16))
        self.level12Button.setMaximumSize(QtCore.QSize(90, 16))
        self.level12Button.setObjectName("level12Button")  # level 12 select
        self.getfileButton.setEnabled(True)
        self.getfileButton.setGeometry(QtCore.QRect(10, 190, 81, 21))
        self.getfileButton.setObjectName("getfileButton")  # get file button
        self.getfileButton.clicked.connect(self.getfileButtonClicked)
        self.fileoutButton.setEnabled(True)
        self.fileoutButton.setGeometry(QtCore.QRect(10, 160, 81, 23))
        self.fileoutButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileoutButton.setAutoFillBackground(False)
        self.fileoutButton.setObjectName("fileoutButton")
        self.introductionButton.setEnabled(True)
        self.introductionButton.setGeometry(QtCore.QRect(10, 130, 81, 23))
        self.introductionButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.introductionButton.setAutoFillBackground(False)
        self.introductionButton.setObjectName("introductionButton")
        self.exitButton.setEnabled(True)
        self.exitButton.setGeometry(QtCore.QRect(10, 220, 81, 23))
        self.exitButton.setObjectName("exitButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.dpButton, self.spButton)
        Dialog.setTabOrder(self.spButton, self.level11Button)
        Dialog.setTabOrder(self.level11Button, self.level12Button)
        Dialog.setTabOrder(self.level12Button, self.tableView)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titlelabel.setText(_translate("Dialog", "Beatmania IIDX Score Table Tools"))
        self.filenamelabel.setText(_translate("Dialog", "File Name"))
        self.spButton.setText(_translate("Dialog", "SP Data"))
        self.dpButton.setText(_translate("Dialog", "DP Data"))
        self.level11Button.setText(_translate("Dialog", "Level 11"))
        self.level12Button.setText(_translate("Dialog", "Level 12"))
        self.getfileButton.setText(_translate("Dialog", "Open"))
        self.fileoutButton.setText(_translate("Dialog", "Make Image"))
        self.introductionButton.setText(_translate("Dialog", "설명"))
        self.exitButton.setText(_translate("Dialog", "Exit"))

    def getfileButtonClicked(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.dialog)
        self.filenamelabel.setText(fname[0])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Init_UI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
