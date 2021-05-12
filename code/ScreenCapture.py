import win32gui, win32ui, win32con, win32api
from cv2 import cv2 as cv
import numpy as np

class screen():
  def __init__(self, n):
    # 分辨率适应
    self.monitor_loc, self.monitor_size = self.getMonitorResolution(n)

    # 获取桌面
    self.hwnd = win32gui.GetDesktopWindow()

    # 创建设备描述表
    self.desktop_dc = win32gui.GetWindowDC(self.hwnd)
    self.img_dc = win32ui.CreateDCFromHandle(self.desktop_dc)
    # 创建一个内存设备描述表
    self.mem_dc = self.img_dc.CreateCompatibleDC()
    # 创建位图对象
    self.screenshot = win32ui.CreateBitmap()
    self.screenshot.CreateCompatibleBitmap(self.img_dc, self.monitor_size[0], self.monitor_size[1])
    self.mem_dc.SelectObject(self.screenshot)

  def capture(self):
    # 截图至内存设备描述表
    self.mem_dc.BitBlt((0, 0), self.monitor_size, self.img_dc, self.monitor_loc[0], win32con.SRCCOPY)
    
    bmpstr = self.screenshot.GetBitmapBits(True)
    img = np.frombuffer(bmpstr, dtype='uint8').reshape(self.monitor_size[1], self.monitor_size[0], 4)[:,:,0:3]
    return img

  def getMonitorResolution(self,n):
    monitorNum = win32api.GetSystemMetrics(0)
    primaryWidth = win32api.GetSystemMetrics(0)
    primaryHeight = win32api.GetSystemMetrics(1)
    primaryMonitor = ((0,0), (primaryWidth-1, primaryHeight-1))
    primarySize = (primaryWidth, primaryHeight)

    virtualWidth = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    virtualHeight = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    virtualMonitor = ((0,0), (virtualWidth-1, virtualHeight-1))
    virtualSize = (virtualWidth, virtualHeight)

    if monitorNum > 1:
      secondaryWidth = virtualWidth - primaryWidth
      secondaryHeight = virtualHeight
      secondaryMonitor = ((primaryWidth,0), (virtualWidth-1, virtualHeight-1))
      secondarySize = (secondaryWidth, secondaryHeight)

    if n == 0:
      return virtualMonitor, virtualSize
    elif n == 1:
      return primaryMonitor, primarySize
    elif monitorNum > 1:
      return secondaryMonitor, secondarySize
    else:
      return None, None

  def __del__(self):
    # 内存释放
    self.img_dc.DeleteDC()
    self.mem_dc.DeleteDC()
    win32gui.ReleaseDC(self.hwnd, self.desktop_dc)
    win32gui.DeleteObject(self.screenshot.GetHandle())



if __name__ == '__main__':
  s = screen(1)
  
  while True:
    img  = s.capture() 
    cv.imshow("s", img)
    cv.waitKey(25)







