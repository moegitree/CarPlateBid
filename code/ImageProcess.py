from cv2 import cv2 as cv
import numpy as np
import time
import json
import threading
import ScreenCapture as sc

class imgFactory():
    def __init__(self, src, offset):
        self.img_c = src
        self.img_g = cv.cvtColor(self.img_c, cv.COLOR_BGR2GRAY)
        self.height = self.img_g.shape[0]
        self.width = self.img_g.shape[1]
        self.offset_x = offset[0] # offset with respect to the whole virtual monitor
        self.offset_y = offset[1]
        self.scale = 1

    def resizeImg(self, scale):
        self.scale = scale
        self.img_c = cv.resize(self.img_c, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)   
        self.img_g = cv.cvtColor(self.img_c, cv.COLOR_BGR2GRAY)
        self.height = self.img_g.shape[0]
        self.width = self.img_g.shape[1]

    def subRegion(self, p1, p2):
        self.offset_x += p1[0]
        self.offset_y += p1[1]
        self.img_c = self.img_c[p1[1]:p2[1], p1[0]:p2[0], :]
        self.img_g = self.img_g[p1[1]:p2[1], p1[0]:p2[0]]

    def downSizeMatch(self, src, tmp, n, thresh = 0.035, scale = 1.15):
        down_tmp = []
        height = tmp.shape[0]
        width = tmp.shape[1]

        for _ in range(n):
            tmp1 = cv.resize(tmp, (width, height), interpolation=cv.INTER_AREA)
                    
            res = cv.matchTemplate(src, tmp1, cv.TM_SQDIFF_NORMED)
            minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(res)
            down_tmp.append((minVal, maxVal, minLoc, maxLoc, width, height))

            height = int(height/scale)
            width = int(width/scale)

        t = 0
        min = down_tmp[0][0]
        for i in range(n):
            if down_tmp[i][0] < min:
                min = down_tmp[i][0]
                t = i
        minVal = down_tmp[t][0]

        if minVal <= thresh:
            minLoc = down_tmp[t][2]
            min_w = down_tmp[t][4]
            min_h = down_tmp[t][5]
            minLoc1 = minLoc
            minLoc2 = (minLoc[0]+min_w, minLoc[1]+min_h)
        else:
            minLoc1=minLoc2=None
        
        return minLoc1, minLoc2, minVal

    def getROI(self, tmp_gray):
        loc1, loc2, minVal = self.downSizeMatch(self.img_g, tmp_gray, 4)

        if (loc1 is not None) and (loc2 is not None):
            #print(minVal)
            x1 = loc1[0] + self.offset_x
            y1 = loc1[1] + self.offset_y
            x2 = loc2[0] + self.offset_x
            y2 = loc2[1] + self.offset_y
            #cv.rectangle(src, (x1, y1), (x2, y2), [0,0,255], thickness=2)
            return (x1, y1), (x2, y2)
        else:
            return None, None     

# if __name__ == '__main__':
#     img = cv.imread(r'C:\Users\chen.zhiyuan\Documents\Python\AutoMouse\pic\add_button.png', cv.IMREAD_COLOR)
#     gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     sift = cv.xfeatures2d.SIFT_create()
#     kp = sift.detect(gray,None)
#     img=cv.drawKeypoints(gray,kp,img)

#     cv.imshow("tt", img)
#     cv.waitKey(0)

class button_thread(threading.Thread):
    def __init__(self, n, buttons):
        threading.Thread.__init__(self)
        self.monitor_num = n
        self.buttons = buttons
    
    def run(self):
        c = sc.screen(self.monitor_num)
        capture = c.capture()
        factory = imgFactory(capture, c.monitor_loc[0])

        p1 = (int(c.monitor_size[0]/2), int(c.monitor_size[1]/4))
        p2 = (int(c.monitor_size[0]*4/5), int(c.monitor_size[1]*3/4)) 
        factory.subRegion(p1, p2)

        for i in range(len(self.buttons)):
            img = cv.imread(self.buttons[i]["path"], cv.IMREAD_GRAYSCALE)

            r1, r2 = factory.getROI(img)
            if (r1 is not None) and (r1 is not None):
                center = (int((r1[0] + r2[0])/2), int((r1[1] + r2[1])/2))
                self.buttons[i]["location"] = center


if __name__ == '__main__':
    offer_path = r".\pic\offer_button.png"
    offer = cv.imread(offer_path, cv.IMREAD_GRAYSCALE)

    add_path = r".\pic\add_button.png"
    add = cv.imread(add_path, cv.IMREAD_GRAYSCALE)

    c = sc.screen(2)

    while True:
        start = time.time()
        ###
        capture = c.capture()
        factory = imgFactory(capture, c.monitor_loc[0])

        p1 = (int(c.monitor_size[0]/2), int(c.monitor_size[1]/4))
        p2 = (int(c.monitor_size[0]*4/5), int(c.monitor_size[1]*3/4)) 
        factory.subRegion(p1, p2)

        r1_1, r1_2 = factory.getROI(add)
        r2_1, r2_2 = factory.getROI(offer)

        if (r1_1 is not None) and (r1_2 is not None):
            add_center = (int((r1_1[0] + r1_2[0])/2), int((r1_1[1] + r1_2[1])/2))

            capture = cv.UMat(capture).get()
            cv.circle(capture, 
                (add_center[0]-c.monitor_loc[0][0], add_center[1]-c.monitor_loc[0][1]), 
                5, [0,0,255], thickness=2)
            # cv.rectangle(capture, 
            #     (r1_1[0]-c.monitor_loc[0][0], r1_1[1]-c.monitor_loc[0][1]),
            #     (r1_2[0]-c.monitor_loc[0][0], r1_2[1]-c.monitor_loc[0][1]), [0,0,255], thickness=2)


        if (r2_1 is not None) and (r2_2 is not None):
            offer_center = (int((r2_1[0] + r2_2[0])/2), int((r2_1[1] + r2_2[1])/2))
            
            capture = cv.UMat(capture).get()
            cv.circle(capture, 
                (offer_center[0]-c.monitor_loc[0][0], offer_center[1]-c.monitor_loc[0][1]), 
                5, [0,0,255], thickness=2)
            # cv.rectangle(capture, 
            #     (r2_1[0]-c.monitor_loc[0][0], r2_1[1]-c.monitor_loc[0][1]),
            #     (r2_2[0]-c.monitor_loc[0][0], r2_2[1]-c.monitor_loc[0][1]), [0,0,255], thickness=2)

        end = time.time()

        print("loop took {} seconds".format(end-start))
        cv.imshow('window', capture)
        cv.imshow("img", factory.img_g)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
