import datetime
import time
import threading

from pynput.mouse import Button as m_Button
from pynput.mouse import Controller as m_Controller
from pynput.keyboard import Key as k_Key
from pynput.keyboard import Controller as k_Controller

import ImageProcess as ip

class bidevent():
    def __init__(self, monitor_num):
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

    def buttonrecognize(self):  #for callback
        t = ip.button_thread(self.monitor_num, self.buttons[0:2])
        t.start()
        t.join()
        print([self.buttons[i]["location"] for i in range(len(self.buttons))])

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


class timer(threading.Thread):
    def __init__(self, bid):
        threading.Thread.__init__(self)
        self.bidobj = bid
        self.timetriggers = {
                    "initial_time": [None, self.bidobj.buttonrecognize, True],      #inital_time,
                    "firstbid_time": [None, self.bidobj.firstbid, True],            #firstbid_time
                    "firstsubmit_time": [None, self.bidobj.firstsubmit, True],      #firstsubmit_time
                    "secondbid_time": [None, self.bidobj.secondbid, True],          #secondbid_time
                    "secondsubmit_time": [None, self.bidobj.secondsubmit, True]     #secondsubmit_time
                }  
        self.timetriggers_list = None     
        self.setInitialTime("12:00:00")
        self.setFirstbidTime("12:00:00")
        self.setFirstsubmitTime("12:00:00")
        self.setSecondbidTime("12:00:00")
        self.setSecondsubmitTime("12:00:00")

    def setInitialTime(self, initial_time):
        t = datetime.datetime.strptime(initial_time, "%H:%M:%S")
        self.timetriggers["initial_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())

    def setFirstbidTime(self, firstbid_time):
        t = datetime.datetime.strptime(firstbid_time, "%H:%M:%S")
        self.timetriggers["firstbid_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())

    def setFirstsubmitTime(self, firstsubmit_time):
        t = datetime.datetime.strptime(firstsubmit_time, "%H:%M:%S")
        self.timetriggers["firstsubmit_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())

    def setSecondbidTime(self, secondbid_time):
        t = datetime.datetime.strptime(secondbid_time, "%H:%M:%S")
        self.timetriggers["secondbid_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())
    
    def setSecondsubmitTime(self, secondsubmit_time):
        t = datetime.datetime.strptime(secondsubmit_time, "%H:%M:%S")
        self.timetriggers["secondsubmit_time"][0] = t
        self.timetriggers_list = list(self.timetriggers.values())

    def run(self):
        for i in range(len(self.timetriggers_list)):

            cont = True
            while cont:
                time_now = datetime.datetime.now()
                print(time_now.strftime('%H:%M:%S.%f'), (self.timetriggers_list[i][0]-time_now).seconds)

                if (self.timetriggers_list[i][0] - time_now).seconds == 0 and self.timetriggers_list[i][2]:
                    self.timetriggers_list[i][2] = False
                    self.timetriggers_list[i][1] ()  # callback self.timetriggers_list[i][1]
                    cont = False  # break
            
                time.sleep(0.01)
            # else:
            #     break

