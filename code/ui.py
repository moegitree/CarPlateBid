# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 280, 451, 131))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.label_5.setObjectName("label_5")
        self.editFirstBidTime = QtWidgets.QTimeEdit(self.groupBox)
        self.editFirstBidTime.setGeometry(QtCore.QRect(260, 60, 91, 22))
        self.editFirstBidTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editFirstBidTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editFirstBidTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editFirstBidTime.setTime(QtCore.QTime(0, 0, 0))
        self.editFirstBidTime.setObjectName("editFirstBidTime")
        self.setFirstBidTime = QtWidgets.QPushButton(self.groupBox)
        self.setFirstBidTime.setGeometry(QtCore.QRect(370, 60, 61, 21))
        self.setFirstBidTime.setObjectName("setFirstBidTime")
        self.editFirstBidValue = QtWidgets.QLineEdit(self.groupBox)
        self.editFirstBidValue.setGeometry(QtCore.QRect(260, 30, 91, 20))
        self.editFirstBidValue.setInputMask("")
        self.editFirstBidValue.setObjectName("editFirstBidValue")
        self.setFirstBidValue = QtWidgets.QPushButton(self.groupBox)
        self.setFirstBidValue.setGeometry(QtCore.QRect(370, 30, 61, 21))
        self.setFirstBidValue.setObjectName("setFirstBidValue")
        self.firstBidTime = QtWidgets.QLabel(self.groupBox)
        self.firstBidTime.setGeometry(QtCore.QRect(140, 60, 101, 21))
        self.firstBidTime.setObjectName("firstBidTime")
        self.firstBidValue = QtWidgets.QLabel(self.groupBox)
        self.firstBidValue.setGeometry(QtCore.QRect(140, 30, 101, 21))
        self.firstBidValue.setObjectName("firstBidValue")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 61, 21))
        self.label_7.setObjectName("label_7")
        self.editFirstSubmitTime = QtWidgets.QTimeEdit(self.groupBox)
        self.editFirstSubmitTime.setGeometry(QtCore.QRect(260, 90, 91, 22))
        self.editFirstSubmitTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editFirstSubmitTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editFirstSubmitTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editFirstSubmitTime.setTime(QtCore.QTime(0, 0, 0))
        self.editFirstSubmitTime.setObjectName("editFirstSubmitTime")
        self.setFirstSubmitTime = QtWidgets.QPushButton(self.groupBox)
        self.setFirstSubmitTime.setGeometry(QtCore.QRect(370, 90, 61, 21))
        self.setFirstSubmitTime.setObjectName("setFirstSubmitTime")
        self.firstSubmitTime = QtWidgets.QLabel(self.groupBox)
        self.firstSubmitTime.setGeometry(QtCore.QRect(140, 90, 101, 21))
        self.firstSubmitTime.setObjectName("firstSubmitTime")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 430, 451, 131))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.label_6.setObjectName("label_6")
        self.editSecondBidTime = QtWidgets.QTimeEdit(self.groupBox_2)
        self.editSecondBidTime.setGeometry(QtCore.QRect(260, 60, 91, 21))
        self.editSecondBidTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editSecondBidTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editSecondBidTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editSecondBidTime.setTime(QtCore.QTime(0, 0, 0))
        self.editSecondBidTime.setObjectName("editSecondBidTime")
        self.setSecondBidTime = QtWidgets.QPushButton(self.groupBox_2)
        self.setSecondBidTime.setGeometry(QtCore.QRect(370, 60, 61, 21))
        self.setSecondBidTime.setObjectName("setSecondBidTime")
        self.editSecondBidValue = QtWidgets.QLineEdit(self.groupBox_2)
        self.editSecondBidValue.setGeometry(QtCore.QRect(260, 30, 91, 20))
        self.editSecondBidValue.setObjectName("editSecondBidValue")
        self.setSecondBidValue = QtWidgets.QPushButton(self.groupBox_2)
        self.setSecondBidValue.setGeometry(QtCore.QRect(370, 30, 61, 21))
        self.setSecondBidValue.setObjectName("setSecondBidValue")
        self.secondBidTime = QtWidgets.QLabel(self.groupBox_2)
        self.secondBidTime.setGeometry(QtCore.QRect(140, 60, 101, 21))
        self.secondBidTime.setObjectName("secondBidTime")
        self.secondBidValue = QtWidgets.QLabel(self.groupBox_2)
        self.secondBidValue.setGeometry(QtCore.QRect(140, 30, 101, 21))
        self.secondBidValue.setObjectName("secondBidValue")
        self.editSecondSubmitTime = QtWidgets.QTimeEdit(self.groupBox_2)
        self.editSecondSubmitTime.setGeometry(QtCore.QRect(260, 90, 91, 21))
        self.editSecondSubmitTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editSecondSubmitTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editSecondSubmitTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editSecondSubmitTime.setTime(QtCore.QTime(0, 0, 0))
        self.editSecondSubmitTime.setObjectName("editSecondSubmitTime")
        self.setSecondSubmitTime = QtWidgets.QPushButton(self.groupBox_2)
        self.setSecondSubmitTime.setGeometry(QtCore.QRect(370, 90, 61, 21))
        self.setSecondSubmitTime.setObjectName("setSecondSubmitTime")
        self.secondSubmitTime = QtWidgets.QLabel(self.groupBox_2)
        self.secondSubmitTime.setGeometry(QtCore.QRect(140, 90, 101, 21))
        self.secondSubmitTime.setObjectName("secondSubmitTime")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 90, 61, 21))
        self.label_8.setObjectName("label_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 80, 451, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"border-color: rgb(255, 2, 19);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(140, 30, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(30, 90, 91, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(30, 120, 91, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.label_13.setObjectName("label_13")
        self.addButtonCoordinate = QtWidgets.QLabel(self.groupBox_3)
        self.addButtonCoordinate.setGeometry(QtCore.QRect(140, 90, 191, 21))
        self.addButtonCoordinate.setObjectName("addButtonCoordinate")
        self.offerButtonCoordinate = QtWidgets.QLabel(self.groupBox_3)
        self.offerButtonCoordinate.setGeometry(QtCore.QRect(140, 120, 191, 21))
        self.offerButtonCoordinate.setObjectName("offerButtonCoordinate")
        self.confirmButtonCoordinate = QtWidgets.QLabel(self.groupBox_3)
        self.confirmButtonCoordinate.setGeometry(QtCore.QRect(140, 150, 191, 19))
        self.confirmButtonCoordinate.setObjectName("confirmButtonCoordinate")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_9.setObjectName("label_9")
        self.setInitialTime = QtWidgets.QPushButton(self.groupBox_3)
        self.setInitialTime.setGeometry(QtCore.QRect(370, 60, 61, 21))
        self.setInitialTime.setObjectName("setInitialTime")
        self.initialTime = QtWidgets.QLabel(self.groupBox_3)
        self.initialTime.setGeometry(QtCore.QRect(140, 60, 101, 21))
        self.initialTime.setObjectName("initialTime")
        self.editInitialTime = QtWidgets.QTimeEdit(self.groupBox_3)
        self.editInitialTime.setGeometry(QtCore.QRect(260, 60, 91, 22))
        self.editInitialTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editInitialTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editInitialTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editInitialTime.setTime(QtCore.QTime(0, 0, 0))
        self.editInitialTime.setObjectName("editInitialTime")
        self.testModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.testModeButton.setGeometry(QtCore.QRect(20, 580, 171, 23))
        self.testModeButton.setObjectName("testModeButton")
        self.defaultModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.defaultModeButton.setGeometry(QtCore.QRect(220, 580, 161, 23))
        self.defaultModeButton.setObjectName("defaultModeButton")
        self.currentTime = QtWidgets.QLabel(self.centralwidget)
        self.currentTime.setGeometry(QtCore.QRect(240, 15, 221, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.currentTime.setFont(font)
        self.currentTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.currentTime.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime.setObjectName("currentTime")
        self.countDown = QtWidgets.QLabel(self.centralwidget)
        self.countDown.setGeometry(QtCore.QRect(240, 50, 221, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.countDown.setFont(font)
        self.countDown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.countDown.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.countDown.setAlignment(QtCore.Qt.AlignCenter)
        self.countDown.setObjectName("countDown")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.groupBox_3.raise_()
        self.testModeButton.raise_()
        self.defaultModeButton.raise_()
        self.currentTime.raise_()
        self.countDown.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.editInitialTime)
        MainWindow.setTabOrder(self.editInitialTime, self.setInitialTime)
        MainWindow.setTabOrder(self.setInitialTime, self.editFirstBidValue)
        MainWindow.setTabOrder(self.editFirstBidValue, self.setFirstBidValue)
        MainWindow.setTabOrder(self.setFirstBidValue, self.editFirstBidTime)
        MainWindow.setTabOrder(self.editFirstBidTime, self.setFirstBidTime)
        MainWindow.setTabOrder(self.setFirstBidTime, self.editFirstSubmitTime)
        MainWindow.setTabOrder(self.editFirstSubmitTime, self.setFirstSubmitTime)
        MainWindow.setTabOrder(self.setFirstSubmitTime, self.editSecondBidValue)
        MainWindow.setTabOrder(self.editSecondBidValue, self.setSecondBidValue)
        MainWindow.setTabOrder(self.setSecondBidValue, self.editSecondBidTime)
        MainWindow.setTabOrder(self.editSecondBidTime, self.setSecondBidTime)
        MainWindow.setTabOrder(self.setSecondBidTime, self.editSecondSubmitTime)
        MainWindow.setTabOrder(self.editSecondSubmitTime, self.setSecondSubmitTime)
        MainWindow.setTabOrder(self.setSecondSubmitTime, self.testModeButton)
        MainWindow.setTabOrder(self.testModeButton, self.defaultModeButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "沪牌拍卖助手"))
        self.label.setText(_translate("MainWindow", "沪牌拍卖助手"))
        self.groupBox.setTitle(_translate("MainWindow", "第一次出价"))
        self.label_3.setText(_translate("MainWindow", "出价时间："))
        self.label_5.setText(_translate("MainWindow", "加价金额："))
        self.editFirstBidTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.setFirstBidTime.setText(_translate("MainWindow", "确定"))
        self.setFirstBidValue.setText(_translate("MainWindow", "确定"))
        self.firstBidTime.setText(_translate("MainWindow", "TextLabel"))
        self.firstBidValue.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "提交时间："))
        self.editFirstSubmitTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.setFirstSubmitTime.setText(_translate("MainWindow", "确定"))
        self.firstSubmitTime.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "第二次出价"))
        self.label_4.setText(_translate("MainWindow", "出价时间："))
        self.label_6.setText(_translate("MainWindow", "加价金额："))
        self.editSecondBidTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.setSecondBidTime.setText(_translate("MainWindow", "确定"))
        self.setSecondBidValue.setText(_translate("MainWindow", "确定"))
        self.secondBidTime.setText(_translate("MainWindow", "TextLabel"))
        self.secondBidValue.setText(_translate("MainWindow", "TextLabel"))
        self.editSecondSubmitTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.setSecondSubmitTime.setText(_translate("MainWindow", "确定"))
        self.secondSubmitTime.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "提交时间："))
        self.groupBox_3.setTitle(_translate("MainWindow", "按钮坐标识别"))
        self.label_10.setText(_translate("MainWindow", "活动显示器"))
        self.comboBox.setItemText(0, _translate("MainWindow", "主显示器"))
        self.comboBox.setItemText(1, _translate("MainWindow", "扩展显示器"))
        self.label_11.setText(_translate("MainWindow", "加价按钮"))
        self.label_12.setText(_translate("MainWindow", "出价按钮"))
        self.label_13.setText(_translate("MainWindow", "验证码确认按钮"))
        self.addButtonCoordinate.setText(_translate("MainWindow", "等待识别..."))
        self.offerButtonCoordinate.setText(_translate("MainWindow", "等待识别..."))
        self.confirmButtonCoordinate.setText(_translate("MainWindow", "等待识别..."))
        self.label_9.setText(_translate("MainWindow", "识别时间："))
        self.setInitialTime.setText(_translate("MainWindow", "确定"))
        self.initialTime.setText(_translate("MainWindow", "TextLabel"))
        self.editInitialTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.testModeButton.setText(_translate("MainWindow", "测试模式（6秒出价）"))
        self.defaultModeButton.setText(_translate("MainWindow", "恢复默认设置"))
        self.currentTime.setText(_translate("MainWindow", "当前时间"))
        self.countDown.setText(_translate("MainWindow", "距下次动作还有 x 秒"))