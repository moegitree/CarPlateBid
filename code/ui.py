# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\code\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.firstGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.firstGroupBox.setGeometry(QtCore.QRect(20, 280, 401, 131))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.firstGroupBox.setFont(font)
        self.firstGroupBox.setStyleSheet("")
        self.firstGroupBox.setObjectName("firstGroupBox")
        self.label_3 = QtWidgets.QLabel(self.firstGroupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.firstGroupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.label_5.setObjectName("label_5")
        self.editFirstBidTime = QtWidgets.QTimeEdit(self.firstGroupBox)
        self.editFirstBidTime.setGeometry(QtCore.QRect(260, 60, 91, 22))
        self.editFirstBidTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editFirstBidTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editFirstBidTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editFirstBidTime.setTime(QtCore.QTime(0, 0, 0))
        self.editFirstBidTime.setObjectName("editFirstBidTime")
        self.editFirstBidValue = QtWidgets.QLineEdit(self.firstGroupBox)
        self.editFirstBidValue.setGeometry(QtCore.QRect(260, 30, 91, 20))
        self.editFirstBidValue.setInputMask("")
        self.editFirstBidValue.setObjectName("editFirstBidValue")
        self.firstBidTime = QtWidgets.QLabel(self.firstGroupBox)
        self.firstBidTime.setGeometry(QtCore.QRect(140, 60, 101, 21))
        self.firstBidTime.setObjectName("firstBidTime")
        self.firstBidValue = QtWidgets.QLabel(self.firstGroupBox)
        self.firstBidValue.setGeometry(QtCore.QRect(140, 30, 101, 21))
        self.firstBidValue.setObjectName("firstBidValue")
        self.label_7 = QtWidgets.QLabel(self.firstGroupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 61, 21))
        self.label_7.setObjectName("label_7")
        self.editFirstSubmitTime = QtWidgets.QTimeEdit(self.firstGroupBox)
        self.editFirstSubmitTime.setGeometry(QtCore.QRect(260, 90, 91, 22))
        self.editFirstSubmitTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editFirstSubmitTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editFirstSubmitTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editFirstSubmitTime.setTime(QtCore.QTime(0, 0, 0))
        self.editFirstSubmitTime.setObjectName("editFirstSubmitTime")
        self.firstSubmitTime = QtWidgets.QLabel(self.firstGroupBox)
        self.firstSubmitTime.setGeometry(QtCore.QRect(140, 90, 101, 21))
        self.firstSubmitTime.setObjectName("firstSubmitTime")
        self.secondGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.secondGroupBox.setGeometry(QtCore.QRect(20, 430, 401, 131))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.secondGroupBox.setFont(font)
        self.secondGroupBox.setStyleSheet("")
        self.secondGroupBox.setObjectName("secondGroupBox")
        self.label_4 = QtWidgets.QLabel(self.secondGroupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.secondGroupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.label_6.setObjectName("label_6")
        self.editSecondBidTime = QtWidgets.QTimeEdit(self.secondGroupBox)
        self.editSecondBidTime.setGeometry(QtCore.QRect(260, 60, 91, 21))
        self.editSecondBidTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editSecondBidTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editSecondBidTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editSecondBidTime.setTime(QtCore.QTime(0, 0, 0))
        self.editSecondBidTime.setObjectName("editSecondBidTime")
        self.editSecondBidValue = QtWidgets.QLineEdit(self.secondGroupBox)
        self.editSecondBidValue.setGeometry(QtCore.QRect(260, 30, 91, 20))
        self.editSecondBidValue.setObjectName("editSecondBidValue")
        self.secondBidTime = QtWidgets.QLabel(self.secondGroupBox)
        self.secondBidTime.setGeometry(QtCore.QRect(140, 60, 101, 21))
        self.secondBidTime.setObjectName("secondBidTime")
        self.secondBidValue = QtWidgets.QLabel(self.secondGroupBox)
        self.secondBidValue.setGeometry(QtCore.QRect(140, 30, 101, 21))
        self.secondBidValue.setObjectName("secondBidValue")
        self.editSecondSubmitTime = QtWidgets.QTimeEdit(self.secondGroupBox)
        self.editSecondSubmitTime.setGeometry(QtCore.QRect(260, 90, 91, 21))
        self.editSecondSubmitTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.editSecondSubmitTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.editSecondSubmitTime.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.editSecondSubmitTime.setTime(QtCore.QTime(0, 0, 0))
        self.editSecondSubmitTime.setObjectName("editSecondSubmitTime")
        self.secondSubmitTime = QtWidgets.QLabel(self.secondGroupBox)
        self.secondSubmitTime.setGeometry(QtCore.QRect(140, 90, 101, 21))
        self.secondSubmitTime.setObjectName("secondSubmitTime")
        self.label_8 = QtWidgets.QLabel(self.secondGroupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 90, 61, 21))
        self.label_8.setObjectName("label_8")
        self.initialGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.initialGroupBox.setGeometry(QtCore.QRect(20, 80, 401, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.initialGroupBox.setFont(font)
        self.initialGroupBox.setStyleSheet("f")
        self.initialGroupBox.setObjectName("initialGroupBox")
        self.label_10 = QtWidgets.QLabel(self.initialGroupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.initialGroupBox)
        self.comboBox.setGeometry(QtCore.QRect(140, 30, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.initialGroupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 90, 91, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.initialGroupBox)
        self.label_12.setGeometry(QtCore.QRect(30, 120, 91, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.initialGroupBox)
        self.label_13.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.label_13.setObjectName("label_13")
        self.addButtonCoordinate = QtWidgets.QLabel(self.initialGroupBox)
        self.addButtonCoordinate.setGeometry(QtCore.QRect(140, 90, 191, 21))
        self.addButtonCoordinate.setObjectName("addButtonCoordinate")
        self.offerButtonCoordinate = QtWidgets.QLabel(self.initialGroupBox)
        self.offerButtonCoordinate.setGeometry(QtCore.QRect(140, 120, 191, 21))
        self.offerButtonCoordinate.setObjectName("offerButtonCoordinate")
        self.confirmButtonCoordinate = QtWidgets.QLabel(self.initialGroupBox)
        self.confirmButtonCoordinate.setGeometry(QtCore.QRect(140, 150, 191, 19))
        self.confirmButtonCoordinate.setObjectName("confirmButtonCoordinate")
        self.label_9 = QtWidgets.QLabel(self.initialGroupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label_9.setObjectName("label_9")
        self.initialTime = QtWidgets.QLabel(self.initialGroupBox)
        self.initialTime.setGeometry(QtCore.QRect(140, 60, 101, 21))
        self.initialTime.setObjectName("initialTime")
        self.editInitialTime = QtWidgets.QTimeEdit(self.initialGroupBox)
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
        self.currentTime.setGeometry(QtCore.QRect(220, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.currentTime.setFont(font)
        self.currentTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.currentTime.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime.setObjectName("currentTime")
        self.countDown = QtWidgets.QLabel(self.centralwidget)
        self.countDown.setGeometry(QtCore.QRect(190, 50, 241, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.countDown.setFont(font)
        self.countDown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.countDown.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.countDown.setAlignment(QtCore.Qt.AlignCenter)
        self.countDown.setObjectName("countDown")
        self.secondGroupBox.raise_()
        self.firstGroupBox.raise_()
        self.label.raise_()
        self.initialGroupBox.raise_()
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
        MainWindow.setTabOrder(self.editInitialTime, self.editFirstBidValue)
        MainWindow.setTabOrder(self.editFirstBidValue, self.editFirstBidTime)
        MainWindow.setTabOrder(self.editFirstBidTime, self.editFirstSubmitTime)
        MainWindow.setTabOrder(self.editFirstSubmitTime, self.editSecondBidValue)
        MainWindow.setTabOrder(self.editSecondBidValue, self.editSecondBidTime)
        MainWindow.setTabOrder(self.editSecondBidTime, self.editSecondSubmitTime)
        MainWindow.setTabOrder(self.editSecondSubmitTime, self.testModeButton)
        MainWindow.setTabOrder(self.testModeButton, self.defaultModeButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "沪牌拍卖助手"))
        self.label.setText(_translate("MainWindow", "沪牌拍卖助手"))
        self.firstGroupBox.setTitle(_translate("MainWindow", "第一次出价"))
        self.label_3.setText(_translate("MainWindow", "出价时间："))
        self.label_5.setText(_translate("MainWindow", "加价金额："))
        self.editFirstBidTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.firstBidTime.setText(_translate("MainWindow", "TextLabel"))
        self.firstBidValue.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "提交时间："))
        self.editFirstSubmitTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.firstSubmitTime.setText(_translate("MainWindow", "TextLabel"))
        self.secondGroupBox.setTitle(_translate("MainWindow", "第二次出价"))
        self.label_4.setText(_translate("MainWindow", "出价时间："))
        self.label_6.setText(_translate("MainWindow", "加价金额："))
        self.editSecondBidTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.secondBidTime.setText(_translate("MainWindow", "TextLabel"))
        self.secondBidValue.setText(_translate("MainWindow", "TextLabel"))
        self.editSecondSubmitTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.secondSubmitTime.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "提交时间："))
        self.initialGroupBox.setTitle(_translate("MainWindow", "按钮坐标识别"))
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
        self.initialTime.setText(_translate("MainWindow", "TextLabel"))
        self.editInitialTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.testModeButton.setText(_translate("MainWindow", "测试模式（6秒出价）"))
        self.defaultModeButton.setText(_translate("MainWindow", "恢复默认设置"))
        self.currentTime.setText(_translate("MainWindow", "当前时间"))
        self.countDown.setText(_translate("MainWindow", "距下次动作还有 x 秒"))
