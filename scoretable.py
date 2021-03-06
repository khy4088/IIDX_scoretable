# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsct.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import csv
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.spButton = QtWidgets.QCheckBox(self.centralwidget)
        self.introductionButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.dpButton = QtWidgets.QCheckBox(self.centralwidget)
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.level11Button = QtWidgets.QCheckBox(self.centralwidget)
        self.fileoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.getfileButton = QtWidgets.QToolButton(self.centralwidget)
        self.level12Button = QtWidgets.QCheckBox(self.centralwidget)
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.mainwindow = MainWindow
        self.__getlevel12Data()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 796)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView.setGeometry(QtCore.QRect(100, 26, 911, 721))
        self.tableView.setObjectName("tableView")
        self.level12Button.setGeometry(QtCore.QRect(10, 96, 69, 16))
        self.level12Button.setMaximumSize(QtCore.QSize(90, 16))
        self.level12Button.setObjectName("level12Button")
        self.getfileButton.setEnabled(True)
        self.getfileButton.setGeometry(QtCore.QRect(10, 186, 81, 21))
        self.getfileButton.setObjectName("getfileButton")
        self.fileoutButton.setEnabled(True)
        self.fileoutButton.setGeometry(QtCore.QRect(10, 156, 81, 23))
        self.fileoutButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileoutButton.setAutoFillBackground(False)
        self.fileoutButton.setObjectName("fileoutButton")
        self.level11Button.setGeometry(QtCore.QRect(10, 74, 69, 16))
        self.level11Button.setMaximumSize(QtCore.QSize(90, 16))
        self.level11Button.setObjectName("level11Button")
        self.titlelabel.setGeometry(QtCore.QRect(9, 5, 195, 16))
        self.titlelabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titlelabel.setObjectName("titlelabel")
        self.dpButton.setGeometry(QtCore.QRect(10, 52, 68, 16))
        self.dpButton.setMaximumSize(QtCore.QSize(90, 16))
        self.dpButton.setObjectName("dpButton")
        self.exitButton.setEnabled(True)
        self.exitButton.setGeometry(QtCore.QRect(10, 216, 81, 23))
        self.exitButton.setObjectName("exitButton")
        self.introductionButton.setEnabled(True)
        self.introductionButton.setGeometry(QtCore.QRect(10, 126, 81, 23))
        self.introductionButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.introductionButton.setAutoFillBackground(False)
        self.introductionButton.setObjectName("introdctionButton")
        self.spButton.setGeometry(QtCore.QRect(10, 30, 68, 16))
        self.spButton.setMaximumSize(QtCore.QSize(90, 16))
        self.spButton.setObjectName("spButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Ready')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.getfileButton.clicked.connect(self.getfileButtonClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beatmania IIDX Tool"))
        self.level12Button.setText(_translate("MainWindow", "Level 12"))
        self.getfileButton.setText(_translate("MainWindow", "Open"))
        self.fileoutButton.setText(_translate("MainWindow", "Make Image"))
        self.level11Button.setText(_translate("MainWindow", "Level 11"))
        self.titlelabel.setText(_translate("MainWindow", "Beatmania IIDX Score Table Tools"))
        self.dpButton.setText(_translate("MainWindow", "DP Data"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.introductionButton.setText(_translate("MainWindow", "설명"))
        self.spButton.setText(_translate("MainWindow", "SP Data"))

    def getfileButtonClicked(self):
        row_counter = 1
        fname = QtWidgets.QFileDialog.getOpenFileName(self.mainwindow, 'Open file', "./", 'CSV Files(*.csv)')
        if fname[0]:
            self.statusbar.showMessage(fname[0] + ' is loaded successfully')
            file_csv = open(fname[0], 'r', encoding='utf-8')
            rdr = csv.reader(file_csv)
            header = next(rdr)
            for row in rdr:
                row_counter += 1
            file_csv = open(fname[0], 'r', encoding='utf-8')
            rdr = csv.reader(file_csv)
            self.__make_table(len(header), row_counter, header, rdr)
        else:
            QMessageBox.about(MainWindow, "Warning", "파일을 선택하세요.")

    def __make_table(self, c_cnt, r_cnt, h_list, reader):
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setColumnCount(c_cnt)
        self.tableView.setRowCount(r_cnt - 1)
        self.tableView.setHorizontalHeaderLabels(h_list)
        self.tableView.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        k = -1
        for row in reader:
            i = range(0, len(row))
            j = 0
            for j in i:
                self.tableView.setItem(k, j, QTableWidgetItem(row[j]))
                j = j + 1
            k += 1
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def __getlevel12Data(self):
        file_csv = open("./sp12.csv", 'r', encoding='utf-8')
        read_csv = csv.reader(file_csv)
        print(read_csv)
        print(type(read_csv))
        csv_list = []
        for row in read_csv:
            csv_list.append(row)
            
        del(csv_list[0])
        print(csv_list)
        return csv_list

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
