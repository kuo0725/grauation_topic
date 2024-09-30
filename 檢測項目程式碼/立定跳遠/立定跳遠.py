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
cap=cv2.VideoCapture(2)
cap.set(3,1280)
cap.set(4,720)
detector_p= PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.7,
                        trackCon=0.7)
#刻度125處距離236高83
dx=[185,216,246,277,312,341,371,402,435,469,496,528,563,599,629,662,693,721,760,795,829,860]
dy=[50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260]
coff=np.polyfit(dx,dy,2) #y=Ax^2+Bx+C
A,B,C=coff
p1=1089
landmarks_p=[]
while True:
    success,img=cap.read()
    if not success:
        break
    pose=detector_p.findPose(img)
    lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
    if lmList_p:
        landmarks_p.extend(lmList_p)
        x1,y1,z1=lmList_p[31]
        x2,y2,z2=lmList_p[29]
        p2=x2
        distance=abs(p2-p1)
        distanceCM=int(round(A*distance**2+B*distance+C,0))
        cvzone.putTextRect(img,f"distance:{distanceCM}CM",(50,50),2.1)
    cv2.imshow("video",img)
    key=cv2.waitKey(1)
    if  key == ord('q'):
            break
    elif key == ord('a'):
        p1=x1
        print(f"({x1})")
    elif key == ord('s'):
        print(distance)
        print(distanceCM,"CM")
        continue
cap.release()
cv2.destroyAllWindows()
