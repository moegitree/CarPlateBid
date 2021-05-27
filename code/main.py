from PyQt5.QtCore import QThread, QTime, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIntValidator

from ui import *
import Bid
import datetime
import sys

def datetime2Qtime(dt):
    ftime = dt.strftime("%H:%M:%S")
    hour = dt.strftime("%H")
    minute = dt.strftime("%M")
    second = dt.strftime("%S")

    return ftime, int(hour), int(minute), int(second)

class showGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        monitor_num = 2         # 1 - primary monitor; 2 - secondary monitor
        bid = Bid.bidevent(monitor_num)   
        self.timer = Bid.bidtimer(bid)

        # connect groupBox to change board color
        self.timer.signal_groupBoxRed0.connect(self.changeInitialGroupBox)
        self.timer.signal_groupBoxRed1.connect(self.changeFirstGroupBox)
        self.timer.signal_groupBoxRed2.connect(self.changeSecondGroupBox)

        # connect gui time button to slot
        self.setInitialTime.pressed.connect(lambda: self.timer.setInitialTime(self.editInitialTime.time()))
        self.setFirstBidTime.pressed.connect(lambda: self.timer.setFirstbidTime(self.editFirstBidTime.time()))
        self.setFirstSubmitTime.pressed.connect(lambda: self.timer.setFirstsubmitTime(self.editFirstSubmitTime.time()))
        self.setSecondBidTime.pressed.connect(lambda: self.timer.setSecondbidTime(self.editSecondBidTime.time()))
        self.setSecondSubmitTime.pressed.connect(lambda: self.timer.setSecondsubmitTime(self.editSecondSubmitTime.time()))

        # connect signal from timer to gui lable slot func      
        self.timer.signal_initialTime.connect(lambda x=self.timer.signal_initialTime: self.showTime(self.initialTime, self.editInitialTime, x))
        self.timer.signal_firstbidTime.connect(lambda x=self.timer.signal_firstbidTime: self.showTime(self.firstBidTime, self.editFirstBidTime, x))
        self.timer.signal_firstsubmitTime.connect(lambda x=self.timer.signal_firstsubmitTime: self.showTime(self.firstSubmitTime, self.editFirstSubmitTime, x))
        self.timer.signal_secondbidTime.connect(lambda x=self.timer.signal_secondbidTime: self.showTime(self.secondBidTime, self.editSecondBidTime, x))
        self.timer.signal_secondsubmitTime.connect(lambda x=self.timer.signal_secondsubmitTime: self.showTime(self.secondSubmitTime, self.editSecondSubmitTime, x))

        # restrict LineEdit can only input num
        self.editFirstBidValue.setValidator(QIntValidator(0, 65535))
        self.editSecondBidValue.setValidator(QIntValidator(0, 65535))

        # connect gui value button to slot
        self.setFirstBidValue.pressed.connect(lambda: self.timer.bidobj.setFirstbid_price(self.editFirstBidValue.text()))
        self.setSecondBidValue.pressed.connect(lambda: self.timer.bidobj.setSecondbid_price(self.editSecondBidValue.text()))

        # connect signal from bid to gui label slot func
        self.timer.bidobj.signal_firstbidPrice.connect(self.showValue_firstBid)
        self.timer.bidobj.signal_secondbidPrice.connect(self.showValue_secondBid)

        # comboBox 
        self.comboBox.setCurrentIndex(monitor_num-1)
        self.comboBox.currentIndexChanged.connect(lambda: self.timer.bidobj.setMonitor_num(self.comboBox.currentIndex()+1))

        # show auction button location
        self.timer.bidobj.signal_buttonCoordinate.connect(self.showCoordinate)

        # connect test mode button
        self.testModeButton.pressed.connect(self.setTestMode)

        # connect default mode button
        self.defaultModeButton.pressed.connect(self.setDefault)

        # connect time signal
        self.timer.signal_currentTime.connect(self.clockLabel)
        self.timer.signal_secsToNextOp.connect(self.countdownLabel)

        self.setDefault()

        self.timer.start()

    def changeInitialGroupBox(self):
        self.initialGroupBox.setStyleSheet("QGroupBox#initialGroupBox{border: 1px solid red;}")
        self.firstGroupBox.setStyleSheet("QGroupBox#firstGroupBox")
        self.secondGroupBox.setStyleSheet("QGroupBox#secondGroupBox")

    def changeFirstGroupBox(self):
        self.initialGroupBox.setStyleSheet("QGroupBox#initialGroupBox")
        self.firstGroupBox.setStyleSheet("QGroupBox#firstGroupBox{border: 1px solid red;}")
        self.secondGroupBox.setStyleSheet("QGroupBox#secondGroupBox")

    def changeSecondGroupBox(self):
        self.initialGroupBox.setStyleSheet("QGroupBox#initialGroupBox")
        self.firstGroupBox.setStyleSheet("QGroupBox#firstGroupBox")
        self.secondGroupBox.setStyleSheet("QGroupBox#secondGroupBox{border: 1px solid red;}")

    def showTime(self, label, edit, t):
        label.setText(t.toString("hh:mm:ss"))
        edit.setTime(t)

    def showValue_firstBid(self, v):
        self.firstBidValue.setText(v)
        self.editFirstBidValue.setText(v)

    def showValue_secondBid(self, v):
        self.secondBidValue.setText(v)
        self.editSecondBidValue.setText(v)

    def showCoordinate(self, l, f):
        if f[0] == 1:
            if (l[0][0] is not None) and (l[0][1] is not None): 
                self.addButtonCoordinate.setStyleSheet("color:black")
                self.addButtonCoordinate.setText( "({0}, {1})".format(str(l[0][0]), str(l[0][1])) )
            else:
                self.addButtonCoordinate.setStyleSheet("color:red")
                self.addButtonCoordinate.setText( "未能识别" )
        if f[1] == 1:
            if (l[1][0] is not None) and (l[1][1] is not None): 
                self.offerButtonCoordinate.setStyleSheet("color:black")
                self.offerButtonCoordinate.setText( "({0}, {1})".format(str(l[1][0]), str(l[1][1])) )
            else:
                self.offerButtonCoordinate.setStyleSheet("color:red")
                self.offerButtonCoordinate.setText("未能识别")
        if f[2] == 1:
            if (l[2][0] is not None) and (l[2][1] is not None): 
                self.confirmButtonCoordinate.setStyleSheet("color:black")
                self.confirmButtonCoordinate.setText( "({0}, {1})".format(str(l[2][0]), str(l[2][1])) )
            else:
                self.confirmButtonCoordinate.setStyleSheet("color:red")
                self.confirmButtonCoordinate.setText("未能识别")

    def setTestMode(self):
        now = QTime.currentTime()
        trigger = now.addSecs(6)
        self.timer.setInitialTime(trigger)

        trigger = now.addSecs(6*2)
        self.timer.setFirstbidTime(trigger)

        trigger = now.addSecs(6*3)
        self.timer.setFirstsubmitTime(trigger)

        trigger = now.addSecs(6*4)
        self.timer.setSecondbidTime(trigger)
        
        trigger = now.addSecs(6*5)
        self.timer.setSecondsubmitTime(trigger)  

    def setDefault(self):
        self.timer.setInitialTime(QTime(11,10,0))
        self.timer.setFirstbidTime(QTime(11,29,43))
        self.timer.setFirstsubmitTime(QTime(11,29,47))
        self.timer.setSecondbidTime(QTime(11,29,53))
        self.timer.setSecondsubmitTime(QTime(11,29,55))
        self.timer.bidobj.setFirstbid_price("1000")
        self.timer.bidobj.setSecondbid_price("1000")

    def clockLabel(self, s):
        self.currentTime.setText(s)

    def countdownLabel(self, i):
        self.countDown.setText("距下次动作还有 {0} 秒".format(i))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = showGUI()
  
    myWin.show()
    sys.exit(app.exec_())
