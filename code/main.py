from PyQt5.QtCore import QThread, QTime, QDateTime, pyqtSignal
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
        match_flag = 0          # 0 - template match; 1 - sift match
        bid = Bid.bidevent(monitor_num, match_flag)   
        self.timer = Bid.bidtimer(bid)

        # connect groupBox to change board color
        self.timer.signal_groupBoxRed0.connect(self.changeInitialGroupBox)
        self.timer.signal_groupBoxRed1.connect(self.changeFirstGroupBox)
        self.timer.signal_groupBoxRed2.connect(self.changeSecondGroupBox)

        # connect gui time button to slot
        self.editInitialTime.timeChanged.connect(self.timer.setInitialTime)
        self.editFirstBidTime.timeChanged.connect(self.timer.setFirstbidTime)
        self.editFirstSubmitTime.timeChanged.connect(self.timer.setFirstsubmitTime)
        self.editSecondBidTime.timeChanged.connect(self.timer.setSecondbidTime)
        self.editSecondSubmitTime.timeChanged.connect(self.timer.setSecondsubmitTime)

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
        self.editFirstBidValue.editingFinished.connect(lambda: self.timer.bidobj.setFirstbid_price(self.editFirstBidValue.text()))
        self.editSecondBidValue.editingFinished.connect(lambda: self.timer.bidobj.setSecondbid_price(self.editSecondBidValue.text()))
     
        # connect signal from bid to gui label slot func
        self.timer.bidobj.signal_firstbidPrice.connect(self.showValue_firstBid)
        self.timer.bidobj.signal_secondbidPrice.connect(self.showValue_secondBid)

        # comboBox 
        self.comboBox.setCurrentIndex(monitor_num-1)
        self.comboBox.currentIndexChanged.connect(lambda: self.timer.bidobj.setMonitor_num(self.comboBox.currentIndex()+1))
        self.comboBox_2.setCurrentIndex(match_flag)
        self.comboBox_2.currentIndexChanged.connect(self.timer.bidobj.setMatch_flag)

        # show auction button location
        self.timer.bidobj.signal_buttonCoordinate.connect(self.showCoordinate)

        # connect test mode button
        self.testModeButton.pressed.connect(self.setTestMode)

        # connect default mode button
        self.defaultModeButton.pressed.connect(self.setDefault)

        # connect time signal
        self.timer.signal_currentTime.connect(self.clockLabel)
        self.timer.signal_secsToNextOp.connect(self.countdownLabel)

        # parameter initialization
        self.setDefault()
        self.timer.bidobj.setMonitor_num(monitor_num)   # initialize monitor_num
        self.timer.bidobj.setMatch_flag(match_flag)     # initialize match_flag

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
                self.addButtonCoordinate.setText( "????????????" )
        if f[1] == 1:
            if (l[1][0] is not None) and (l[1][1] is not None): 
                self.offerButtonCoordinate.setStyleSheet("color:black")
                self.offerButtonCoordinate.setText( "({0}, {1})".format(str(l[1][0]), str(l[1][1])) )
            else:
                self.offerButtonCoordinate.setStyleSheet("color:red")
                self.offerButtonCoordinate.setText("????????????")
        if f[2] == 1:
            if (l[2][0] is not None) and (l[2][1] is not None): 
                self.confirmButtonCoordinate.setStyleSheet("color:black")
                self.confirmButtonCoordinate.setText( "({0}, {1})".format(str(l[2][0]), str(l[2][1])) )
            else:
                self.confirmButtonCoordinate.setStyleSheet("color:red")
                self.confirmButtonCoordinate.setText("????????????")

    def setTestMode(self):
        now = QTime.currentTime()
        sec = 6
        trigger = now.addSecs(sec)
        self.timer.setInitialTime(trigger)

        trigger = now.addSecs(sec*2)
        self.timer.setFirstbidTime(trigger)

        trigger = now.addSecs(sec*3)
        self.timer.setFirstsubmitTime(trigger)

        trigger = now.addSecs(sec*4)
        self.timer.setSecondbidTime(trigger)
        
        trigger = now.addSecs(sec*5)
        self.timer.setSecondsubmitTime(trigger)  

    def setDefault(self):
        self.timer.setInitialTime(QTime(11,27,0,600))
        self.timer.setFirstbidTime(QTime(11,29,41,600))
        self.timer.setFirstsubmitTime(QTime(11,29,46,600))
        self.timer.setSecondbidTime(QTime(11,29,50,600))
        self.timer.setSecondsubmitTime(QTime(11,29,57,600))
        self.timer.bidobj.setFirstbid_price("400")
        self.timer.bidobj.setSecondbid_price("500")

    def clockLabel(self, s):
        self.currentTime.setText(s)

    def countdownLabel(self, i):
        self.countDown.setText("????????????????????? {0} ???".format(i))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = showGUI()
  
    myWin.show()
    sys.exit(app.exec_())
