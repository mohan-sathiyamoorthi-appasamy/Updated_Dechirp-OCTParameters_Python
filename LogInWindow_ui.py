# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:\Test_LogIn\LogInWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1563, 897)
        MainWindow.setStyleSheet("background-color: rgba(0,0,0,140);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,219),stop:1 rgba(85,98,112,226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
" \n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"     padding-left:5px;\n"
"     padding-top:5px;\n"
"     background-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"  \n"
"\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(710, 330, 431, 441))
        self.label.setStyleSheet("background-color:rgba(16,30,41,240);\n"
"border-image: url(:/Exit/Final.jpg);\n"
"border-radius:10px;\n"
"")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_Exit = QtWidgets.QPushButton(self.home)
        self.pushButton_Exit.setGeometry(QtCore.QRect(1110, 330, 31, 31))
        self.pushButton_Exit.setStyleSheet("border-image: url(:/Exit/exit.jpg);\n"
"\n"
"")
        self.pushButton_Exit.setText("")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.label_2 = QtWidgets.QLabel(self.home)
        self.label_2.setGeometry(QtCore.QRect(710, 370, 431, 401))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,150);\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.home)
        self.label_3.setGeometry(QtCore.QRect(870, 410, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.home)
        self.lineEdit.setGeometry(QtCore.QRect(760, 489, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding:2px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.home)
        self.lineEdit_2.setGeometry(QtCore.QRect(760, 560, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding:2px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.home)
        self.pushButton.setGeometry(QtCore.QRect(830, 630, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.home)
        self.label_4.setGeometry(QtCore.QRect(840, 680, 181, 31))
        self.label_4.setStyleSheet("color:rgba(255,255,255,140);")
        self.label_4.setObjectName("label_4")
        self.error = QtWidgets.QLabel(self.home)
        self.error.setGeometry(QtCore.QRect(830, 600, 191, 21))
        self.error.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:red")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.stackedWidget.addWidget(self.home)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("QPushButton#pushButton_loadInterference{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,219),stop:1 rgba(85,98,112,226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_loadInterference:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
" \n"
"}\n"
"\n"
"QPushButton#pushButton_loadInterference:pressed{\n"
"     padding-left:5px;\n"
"     padding-top:5px;\n"
"     background-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_loadmovarm{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,219),stop:1 rgba(85,98,112,226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_loadmovarm:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
" \n"
"}\n"
"\n"
"QPushButton#pushButton_loadmovarm:pressed{\n"
"     padding-left:5px;\n"
"     padding-top:5px;\n"
"     background-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_loadrefarm{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,219),stop:1 rgba(85,98,112,226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_loadrefarm:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
" \n"
"}\n"
"\n"
"QPushButton#pushButton_loadrefarm:pressed{\n"
"     padding-left:5px;\n"
"     padding-top:5px;\n"
"     background-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"QPushButton#pushButton_generatedechirp{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,219),stop:1 rgba(85,98,182,226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_generatedechirp:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
" \n"
"}\n"
"\n"
"QPushButton#pushButton_generatedechirp:pressed{\n"
"     padding-left:5px;\n"
"     padding-top:5px;\n"
"     background-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_savedechirp{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,219),stop:1 rgba(105,198,112,226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_savedechirp:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
" \n"
"}\n"
"\n"
"QPushButton#pushButton_savedechirp:pressed{\n"
"     padding-left:5px;\n"
"     padding-top:5px;\n"
"     background-color:rgba(105,118,132,200);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_octparameters{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,219),stop:1 rgba(185,98,112,226));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_octparameters:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
" \n"
"}\n"
"\n"
"QPushButton#pushButton_octparameters:pressed{\n"
"     padding-left:5px;\n"
"     padding-top:5px;\n"
"     background-color:rgba(105,118,132,200);\n"
"}\n"
"")
        self.page_2.setObjectName("page_2")
        self.pushButton_loadInterference = QtWidgets.QPushButton(self.page_2)
        self.pushButton_loadInterference.setGeometry(QtCore.QRect(90, 160, 161, 41))
        self.pushButton_loadInterference.setStyleSheet("color:rgba(255,255,255,140);")
        self.pushButton_loadInterference.setObjectName("pushButton_loadInterference")
        self.pushButton_loadmovarm = QtWidgets.QPushButton(self.page_2)
        self.pushButton_loadmovarm.setGeometry(QtCore.QRect(90, 220, 161, 41))
        self.pushButton_loadmovarm.setStyleSheet("color:rgba(255,255,255,140);")
        self.pushButton_loadmovarm.setObjectName("pushButton_loadmovarm")
        self.pushButton_loadrefarm = QtWidgets.QPushButton(self.page_2)
        self.pushButton_loadrefarm.setGeometry(QtCore.QRect(90, 280, 161, 41))
        self.pushButton_loadrefarm.setStyleSheet("color:rgba(255,255,255,140);")
        self.pushButton_loadrefarm.setObjectName("pushButton_loadrefarm")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(90, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 100, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color:black;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_Exit_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_Exit_2.setGeometry(QtCore.QRect(1260, 60, 51, 51))
        self.pushButton_Exit_2.setStyleSheet("border-image: url(:/Exit/exit.jpg);")
        self.pushButton_Exit_2.setText("")
        self.pushButton_Exit_2.setObjectName("pushButton_Exit_2")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(290, 160, 500, 300))
        self.widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(820, 160, 500, 300))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setGeometry(QtCore.QRect(290, 490, 500, 300))
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.page_2)
        self.widget_4.setGeometry(QtCore.QRect(820, 490, 500, 300))
        self.widget_4.setAutoFillBackground(False)
        self.widget_4.setObjectName("widget_4")
        self.pushButton_generatedechirp = QtWidgets.QPushButton(self.page_2)
        self.pushButton_generatedechirp.setGeometry(QtCore.QRect(90, 490, 161, 41))
        self.pushButton_generatedechirp.setStyleSheet("color:rgba(255,255,255,140);")
        self.pushButton_generatedechirp.setObjectName("pushButton_generatedechirp")
        self.pushButton_octparameters = QtWidgets.QPushButton(self.page_2)
        self.pushButton_octparameters.setGeometry(QtCore.QRect(90, 610, 161, 41))
        self.pushButton_octparameters.setStyleSheet("color:rgba(255,255,255,140);")
        self.pushButton_octparameters.setObjectName("pushButton_octparameters")
        self.pushButton_savedechirp = QtWidgets.QPushButton(self.page_2)
        self.pushButton_savedechirp.setGeometry(QtCore.QRect(90, 550, 161, 41))
        self.pushButton_savedechirp.setStyleSheet("color:rgba(255,255,255,140);")
        self.pushButton_savedechirp.setObjectName("pushButton_savedechirp")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "L o g I n"))
        self.label_4.setText(_translate("MainWindow", "Forgot Your User Name or Password?"))
        self.pushButton_loadInterference.setText(_translate("MainWindow", "Load Interference Raw File"))
        self.pushButton_loadmovarm.setText(_translate("MainWindow", "Load Moving Arm Raw File"))
        self.pushButton_loadrefarm.setText(_translate("MainWindow", "Load Reference Arm Raw File"))
        self.label_5.setText(_translate("MainWindow", "  Enter Spectrometer ID:"))
        self.pushButton_generatedechirp.setText(_translate("MainWindow", "Generate Dechirp File"))
        self.pushButton_octparameters.setText(_translate("MainWindow", "OCT System Parameters"))
        self.pushButton_savedechirp.setText(_translate("MainWindow", "Save Dechirp Text File "))


#from . import res_rc
