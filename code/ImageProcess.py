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

    #update img in class imgFactory, assume the new one has the same height and width as the old one
    def updateImg(self, src): 
        self.img_c = src
        self.img_g = cv.cvtColor(self.img_c, cv.COLOR_BGR2GRAY)

    def resizeImg(self, scale):
        self.scale = scale
        self.img_c = cv.resize(self.img_c, None, fx=scale, fy=scale, interpolation=cv.INTER_CUBIC) #inter_cubic is faster than inter_area
        # self.img_c = cv.resize(self.img_c, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)   
        self.img_g = cv.cvtColor(self.img_c, cv.COLOR_BGR2GRAY)
        self.height = self.img_g.shape[0]
        self.width = self.img_g.shape[1]

    def subRegion(self, p1, p2):
        self.offsetSubRegion_x = self.offset_x + p1[0]
        self.offsetSubRegion_y = self.offset_y + p1[1]
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

    def templateMatch(self, tmp):
        loc1, loc2, minVal = self.downSizeMatch(self.img_g, tmp, 4)

        if (loc1 is not None) and (loc2 is not None):
            #print(minVal)
            x1 = loc1[0] + self.offsetSubRegion_x
            y1 = loc1[1] + self.offsetSubRegion_y
            x2 = loc2[0] + self.offsetSubRegion_x
            y2 = loc2[1] + self.offsetSubRegion_y
            #cv.rectangle(src, (x1, y1), (x2, y2), [0,0,255], thickness=2)
            return (x1, y1), (x2, y2)
        else:
            return None, None     

    def siftMatch(self, tmp):
        MIN_MATCH_COUNT = 10

        img1 = tmp
        img2 = self.img_g

        # Initiate SIFT detector
        sift = cv.xfeatures2d.SIFT_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des1,des2,k=2)

        # store all the good matches as per Lowe's ratio test.
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)

        # use RANSAC to eliminate wrong matched points
        if len(good)>MIN_MATCH_COUNT:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
            matchesMask = mask.ravel().tolist()
        else:
            print ("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
            matchesMask = None


        # calculate matched keypoints' center
        count = 0
        sum_x = 0
        sum_y = 0
        for i in range(len(good)):
            if matchesMask is not None:     # matchesMask == None
                if matchesMask[i] == 1:
                    sum_x += kp2[good[i].trainIdx].pt[0]
                    sum_y += kp2[good[i].trainIdx].pt[1]
                    count += 1               
                else:
                    pass
            else:                           # matchesMask != None
                sum_x += kp2[good[i].trainIdx].pt[0]
                sum_y += kp2[good[i].trainIdx].pt[1]
                count += 1   

        if count != 0:
            return (int(sum_x/count)+self.offsetSubRegion_x, int(sum_y/count)+self.offsetSubRegion_y)
        else: 
            return (None, None)

    def getROICenter(self, tmp, flag=0):
        center = (None, None)

        if flag==0 :          # template match
            r1, r2 = self.templateMatch(tmp)

            if (r1 is not None) and (r2 is not None):
                center = (int((r1[0] + r2[0])/2), int((r1[1] + r2[1])/2))

        elif flag == 1:        # detect sift keypoint and match points using RANSAC
            center = self.siftMatch(tmp)
            
        return center

# thread for localizing specific button, return button's coordinate
class button_thread(threading.Thread):
    def __init__(self, n, buttons, loop_flag=0, match_flag=0):
        threading.Thread.__init__(self)
        self.monitor_num = n
        self.buttons = buttons
        self.loop_flag = loop_flag
        self.match_flag = match_flag    # 0 - template match; 1 - sift descriptor match
    
    def run(self):
        if self.loop_flag == 0:
            self.buttonLoc_once()
        else:
            self.buttonLoc_loop()

    #localize specific button, return None if it not exist
    def buttonLoc_once(self):
        c = sc.screen(self.monitor_num)
        capture = c.capture()
        factory = imgFactory(capture, c.monitor_loc[0])

        p1 = (int(c.monitor_size[0]/2), int(c.monitor_size[1]*1/6))
        p2 = (int(c.monitor_size[0]*4/5), int(c.monitor_size[1]*5/6)) 
        factory.subRegion(p1, p2)

        for i in range(len(self.buttons)):
            img = cv.imread(self.buttons[i]["path"], cv.IMREAD_GRAYSCALE)

            self.buttons[i]["location"] = factory.getROICenter(img, self.match_flag)

    #localize specific button, returen coordinate until it appears on screen
    def buttonLoc_loop(self):
        c = sc.screen(self.monitor_num)
        capture = c.capture()
        factory = imgFactory(capture, c.monitor_loc[0])

        p1 = (int(c.monitor_size[0]/2), int(c.monitor_size[1]*1/6))
        p2 = (int(c.monitor_size[0]*4/5), int(c.monitor_size[1]*5/6)) 
        
        cont = True
        while cont:
            capture = c.capture()
            factory.updateImg(capture)
            factory.subRegion(p1, p2)

            for i in range(len(self.buttons)):
                img = cv.imread(self.buttons[i]["path"], cv.IMREAD_GRAYSCALE)

                center = factory.getROICenter(img, self.match_flag)
                self.buttons[i]["location"] = center

                if (center[0] is not None) and (center[1] is not None):
                    cont = False
                else:
                    cont = True

if __name__ == '__main__':
    tmp1_path = r".\pic\offer.png"
    tmp1 = cv.imread(tmp1_path, cv.IMREAD_GRAYSCALE)

    tmp2_path = r".\pic\add.png"
    tmp2 = cv.imread(tmp2_path, cv.IMREAD_GRAYSCALE)

    c = sc.screen(2)

    while True:
        start = time.time()
        
        capture = c.capture()

        factory = imgFactory(capture, c.monitor_loc[0])

        p1 = (int(c.monitor_size[0]/2), int(c.monitor_size[1]*1/6))
        p2 = (int(c.monitor_size[0]*4/5), int(c.monitor_size[1]*5/6)) 
        factory.subRegion(p1, p2)

        tmp1_c = factory.getROICenter(tmp1, 1)
        tmp2_c = factory.getROICenter(tmp2, 1)

        if (tmp1_c[0] is not None) and (tmp1_c[1] is not None):
            capture = cv.UMat(capture).get()
            cv.circle(capture, 
                (tmp1_c[0]-c.monitor_loc[0][0], tmp1_c[1]-c.monitor_loc[0][1]), 
                5, [0,0,255], thickness=2)


        if (tmp2_c[0] is not None) and (tmp2_c[1] is not None):
            capture = cv.UMat(capture).get()
            cv.circle(capture, 
                (tmp2_c[0]-c.monitor_loc[0][0], tmp2_c[1]-c.monitor_loc[0][1]), 
                5, [0,0,255], thickness=2)

        end = time.time()

        print("loop took {} seconds".format(end-start))
        cv.imshow('window', capture)
        cv.imshow("img", factory.img_g)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
