import datetime
import time
import threading

from pynput.mouse import Button as m_Button
from pynput.mouse import Controller as m_Controller
from pynput.keyboard import Key as k_Key
from pynput.keyboard import Controller as k_Controller
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QTime

import ImageProcess as ip

class bidevent(QObject):
    signal_firstbidPrice = pyqtSignal(str)
    signal_secondbidPrice = pyqtSignal(str)
    signal_buttonCoordinate = pyqtSignal(list, list)

    def __init__(self, monitor_num):
        super().__init__()
        self.monitor_num = monitor_num
        self.buttons = [
                    {   "name": "offer_button",
                        "path": r".\pic\offer_button.png", 
                        "location": (None, None)
                    },
                    {   "name":  "add_button",
                        "path": r".\pic\add_button.png",
                        "location": (None, None)
                    },
                    {   "name":  "ok_button",
                        "path": r".\pic\ok_button.png",
                        "location": (None, None)
                    }
                ] 
        self.bidprice = { 
                    "firstbid_price":   300, 
                    "secondbid_price":  1000
            }   

    def bidevent_initialize(self):
        self.setFirstbid_price("300")
        self.setSecondbid_price("1000")

    def setMonitor_num(self, n):
        self.monitor_num = n
        print(self.monitor_num)

    def setFirstbid_price(self, value):
        self.bidprice["firstbid_price"] = value
        self.signal_firstbidPrice.emit(value)        

    def setSecondbid_price(self, value):
        self.bidprice["secondbid_price"] = value
        self.signal_secondbidPrice.emit(value)

    def buttonrecognize(self):  #for callback
        t = ip.button_thread(self.monitor_num, self.buttons[0:2])
        t.start()
        t.join()
        print([self.buttons[i]["location"] for i in range(len(self.buttons))])
        self.signal_buttonCoordinate.emit([self.buttons[i]["location"] for i in range(len(self.buttons))], [1,1,0])

    def firstbid(self):  #for callback
        mouse = m_Controller()
        keyboard = k_Controller()

        mouse.position = (self.buttons[1]["location"][0]-100, self.buttons[1]["location"][1])      # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

        keyboard.type("\b\b\b\b\b")
        keyboard.type(str(self.bidprice["firstbid_price"]))

        mouse.position = self.buttons[1]["location"]
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

        mouse.position = self.buttons[0]["location"]    # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

        time.sleep(0.15)
        
        t = ip.button_thread(self.monitor_num, [self.buttons[2]])
        t.start()
        t.join()
        self.signal_buttonCoordinate.emit([self.buttons[i]["location"] for i in range(len(self.buttons))], [0,0,1])

        mouse.position = (self.buttons[2]["location"][0]+200, self.buttons[2]["location"][1]-100)   # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

    def firstsubmit(self):  #for callback
        mouse = m_Controller()

        mouse.position = (self.buttons[2]["location"][0], self.buttons[2]["location"][1])   # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

    def secondbid(self):  #for callback
        mouse = m_Controller()
        keyboard = k_Controller()

        mouse.position = (self.buttons[1]["location"][0]-100, self.buttons[1]["location"][1])      # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

        keyboard.type("\b\b\b\b\b")
        keyboard.type(str(self.bidprice["secondbid_price"]))

        mouse.position = self.buttons[1]["location"]
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

        mouse.position = self.buttons[0]["location"]    # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

        time.sleep(0.15)

        mouse.position = (self.buttons[2]["location"][0]+200, self.buttons[2]["location"][1]-100)   # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)

    def secondsubmit(self):  #for callback
        mouse = m_Controller()

        mouse.position = (self.buttons[2]["location"][0], self.buttons[2]["location"][1])   # if button location not found, exit script with error 
        mouse.press(m_Button.left)
        mouse.release(m_Button.left)


class bidtimer(QThread):
    signal_initialTime = pyqtSignal(QTime)
    signal_firstbidTime = pyqtSignal(QTime)
    signal_firstsubmitTime = pyqtSignal(QTime)
    signal_secondbidTime = pyqtSignal(QTime)
    signal_secondsubmitTime = pyqtSignal(QTime)

    signal_currentTime = pyqtSignal(str)
    signal_secsToNextOp = pyqtSignal(int)

    signal_groupBoxRed0 = pyqtSignal()
    signal_groupBoxRed1 = pyqtSignal()
    signal_groupBoxRed2 = pyqtSignal()

    def __init__(self, bid):
        super().__init__()  # initial QThread
        self.bidobj = bid
        self.timetriggers = {
                    "initial_time": [None, self.bidobj.buttonrecognize, True],      #inital_time,
                    "firstbid_time": [None, self.bidobj.firstbid, True],            #firstbid_time
                    "firstsubmit_time": [None, self.bidobj.firstsubmit, True],      #firstsubmit_time
                    "secondbid_time": [None, self.bidobj.secondbid, True],          #secondbid_time
                    "secondsubmit_time": [None, self.bidobj.secondsubmit, True]     #secondsubmit_time
                }  
        self.timetriggers_list = None    

    def time_initialize(self):
        self.setInitialTime(QTime(12,0,0)) # initialize to 12:00:00
        self.setFirstbidTime(QTime(12,0,0))
        self.setFirstsubmitTime(QTime(12,0,0))
        self.setSecondbidTime(QTime(12,0,0))
        self.setSecondsubmitTime(QTime(12,0,0))

    def setInitialTime(self, initial_qtime):
        initial_time = initial_qtime.toString("hh:mm:ss")
        t = datetime.datetime.strptime(initial_time, "%H:%M:%S")
        self.timetriggers["initial_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())
        self.signal_initialTime.emit(initial_qtime)

    def setFirstbidTime(self, firstbid_qtime):
        firstbid_time = firstbid_qtime.toString("hh:mm:ss")
        t = datetime.datetime.strptime(firstbid_time, "%H:%M:%S")
        self.timetriggers["firstbid_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())
        self.signal_firstbidTime.emit(firstbid_qtime)

    def setFirstsubmitTime(self, firstsubmit_qtime):
        firstsubmit_time = firstsubmit_qtime.toString("hh:mm:ss")
        t = datetime.datetime.strptime(firstsubmit_time, "%H:%M:%S")
        self.timetriggers["firstsubmit_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())
        self.signal_firstsubmitTime.emit(firstsubmit_qtime)

    def setSecondbidTime(self, secondbid_qtime):
        secondbid_time = secondbid_qtime.toString("hh:mm:ss")
        t = datetime.datetime.strptime(secondbid_time, "%H:%M:%S")
        self.timetriggers["secondbid_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())
        self.signal_secondbidTime.emit(secondbid_qtime)

    def setSecondsubmitTime(self, secondsubmit_qtime):
        secondsubmit_time = secondsubmit_qtime.toString("hh:mm:ss")
        t = datetime.datetime.strptime(secondsubmit_time, "%H:%M:%S")
        self.timetriggers["secondsubmit_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())
        self.signal_secondsubmitTime.emit(secondsubmit_qtime)

    def run(self):
        for i in range(len(self.timetriggers_list)):

            if i == 0 :
                self.signal_groupBoxRed0.emit()
            elif i == 1 or i == 2:
                self.signal_groupBoxRed1.emit()
            elif i == 3 or i == 4:
                self.signal_groupBoxRed2.emit()

            cont = True
            while cont:
                time_now = datetime.datetime.now()
                time_now_str = time_now.strftime('%H:%M:%S')
                secs = (self.timetriggers_list[i][0]-time_now).seconds
                #print(time_now.strftime('%H:%M:%S.%f'), secs)
                self.signal_currentTime.emit(time_now_str)
                self.signal_secsToNextOp.emit(secs)

                if (self.timetriggers_list[i][0] - time_now).seconds == 0 and self.timetriggers_list[i][2]:
                    self.timetriggers_list[i][2] = False
                    self.timetriggers_list[i][1] ()  # callback self.timetriggers_list[i][1]
                    cont = False  # break
            
                time.sleep(0.01)
            # else:
            #     break

