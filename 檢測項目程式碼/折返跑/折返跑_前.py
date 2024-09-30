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
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector_p= PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
#total_level=[9,8.5,8.5,8,8,7.5,7.5,7,7,7,6.5,6.5,6,6,6,5.5,5.5,5]
level=[18.0,17.0,17.0,16.0,16.0,15.0,15.0,14.0,14.0,14.0,13.0,13.0,12.0,12.0,12.0,11.0,11.0,10.0]
#total_round=[7,15,23,32,41,51,61,72,83,94,106,118,131,144,157,171,185,200]
round=[3,7,11,16,20,25,30,36,41,47,53,59,65,72,78,85,92,100]
#landmarks_p=[]
start=cv2.getTickCount()
goal=False
begin=False
lv=1
r=0
fail=0
while True:
    success,img=cap.read()
    if not success:
        break
    goal=False
    end=cv2.getTickCount()
    time=math.floor(((end-start)/cv2.getTickFrequency())*10)/10
    cv2.line(img,(280,595),(1060,595),(0,0,255),5)
    pose=detector_p.findPose(img)
    lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
    if time==level[lv-1] and begin:
        if lmList_p:
            x1,y1,z1=lmList_p[32]
            x2,y2,z2=lmList_p[31]
            p1=y1
            p2=y2
            if p1>595 and p2>595:
                goal=True
            else:
                goal=False
        if goal:
            r+=1
        else:
            r+=1
            fail+=1
        start=cv2.getTickCount() 
    if r==round[lv-1]:
        lv+=1
    """
    if fail==2:
        begin=False
    """
    #cvzone.putTextRect(img,f"{goal}",(1100,200))
    cvzone.putTextRect(img,f"round:{r}",(100,100))
    cvzone.putTextRect(img,f"fail:{fail}",(1100,300))
    cvzone.putTextRect(img,f"{time}s",(1100,100))
    cv2.imshow("video",img)
    #cv2.setMouseCallback('video', show_xy)
    key=cv2.waitKey(1)
    if  key == ord('q'):
            break
    elif key == ord('a'):
        start=cv2.getTickCount()
        lv=1
        r=0
        fail=0
        begin=True
    elif key == ord('s'):
        begin=False
        print("round:",r)
        print("fail:",fail)
cap.release()
cv2.destroyAllWindows()