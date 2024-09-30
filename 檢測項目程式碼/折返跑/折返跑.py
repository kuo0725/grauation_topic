#mediapipe 0.10.11
#cvaone 1.5.2
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector
import math
import numpy as np
import cvzone
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def show_xy(event,x,y,flags,userdata):
    print(event,x,y,flags)
cap=cv2.VideoCapture("begin.mp4")
cap.set(3,1280)
cap.set(4,720)
detector_p= PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
#刻度125處距離236高83
#dx=[185,216,246,277,312,341,371,402,435,469,496,528,563,599,629,662,693,721,760,795,829,860]
#dy=[50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260]
#coff=np.polyfit(dx,dy,2) #y=Ax^2+Bx+C
#A,B,C=coff
p1=0
landmarks_p=[]
start=cv2.getTickCount()
goal=False
while True:
    success,img=cap.read()
    if not success:
        break
    end=cv2.getTickCount()
    cv2.line(img,(280,595),(1060,595),(0,0,255),5)
    pose=detector_p.findPose(img)
    lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
    if lmList_p:
        landmarks_p.extend(lmList_p)
        x1,y1,z1=lmList_p[32]
        x2,y2,z2=lmList_p[21]
        p1=y1
        p2=y2
        #distance=abs(p2-p1)
        #distanceCM=int(round(A*distance**2+B*distance+C,0))
        if p1>595 or p2>595:
            goal=True
        else:
            goal=False
    time=int((end-start)/cv2.getTickFrequency())
    cvzone.putTextRect(img,f"{goal}",(1100,600))
    cvzone.putTextRect(img,f"{time}s",(1100,100))
    cv2.imshow("video",img)
    #cv2.setMouseCallback('video', show_xy)
    key=cv2.waitKey(1)
    if  key == ord('q'):
            break
    elif key == ord('a'):
        start=cv2.getTickCount()
    elif key == ord('s'):
        continue
cap.release()
cv2.destroyAllWindows()