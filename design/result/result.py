# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time_p = QtWidgets.QLabel(self.centralwidget)
        self.time_p.setGeometry(QtCore.QRect(20, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.time_p.setFont(font)
        self.time_p.setText("")
        self.time_p.setObjectName("time_p")
        self.written = QtWidgets.QLabel(self.centralwidget)
        self.written.setGeometry(QtCore.QRect(20, 50, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.written.setFont(font)
        self.written.setText("")
        self.written.setObjectName("written")
        self.wrongs = QtWidgets.QLabel(self.centralwidget)
        self.wrongs.setGeometry(QtCore.QRect(20, 90, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.wrongs.setFont(font)
        self.wrongs.setText("")
        self.wrongs.setObjectName("wrongs")
        self.v = QtWidgets.QLabel(self.centralwidget)
        self.v.setGeometry(QtCore.QRect(20, 130, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.v.setFont(font)
        self.v.setText("")
        self.v.setObjectName("v")
        self.btn_finish = QtWidgets.QPushButton(self.centralwidget)
        self.btn_finish.setGeometry(QtCore.QRect(20, 170, 200, 35))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.btn_finish.setFont(font)
        self.btn_finish.setStyleSheet("background-color: rgba(255,255,255,100);border: 1px solid #1565C0;border-radius: 8px;")
        self.btn_finish.setObjectName("btn_finish")
        self.btn_continue = QtWidgets.QPushButton(self.centralwidget)
        self.btn_continue.setGeometry(QtCore.QRect(240, 170, 200, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_continue.sizePolicy().hasHeightForWidth())
        self.btn_continue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.btn_continue.setFont(font)
        self.btn_continue.setStyleSheet("background-color: rgba(255,255,255,100);border: 1px solid #1565C0;border-radius: 8px;")
        self.btn_continue.setObjectName("btn_continue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Результат"))
        self.btn_finish.setText(_translate("MainWindow", "Закрыть программу"))
        self.btn_continue.setText(_translate("MainWindow", "Продолжить"))
