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
cap=cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
detector_p= PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
#dx=[32,56,82,112,141,175,210,248,286,328,378,425]
#dy=[5,10,15,20,25,30,35,40,45,50,55,60]
#coff=np.polyfit(dx,dy,2) #y=Ax^2+Bx+C
#A,B,C=coff
landmarks_p=[]
times=0
d=False
rdown=True
ldown=True
while True:
    success,img=cap.read()
    if not success:
        break
    pose=detector_p.findPose(img)
    lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
    if lmList_p:
        landmarks_p.extend(lmList_p)
        x1,y1,z1=lmList_p[25]
        x2,y2,z2=lmList_p[26]
        p1=[x1,y1,z1]
        p2=[x2,y2,z2]
        cvzone.putTextRect(img,f"times:{int(times/2)}",(100,300))
        if d :
            cv2.line(img,(280,s),(1060,s),(0,0,255),5)
            if p2[1]<=s and rdown:
                times+=1
                rdown=False
                ldown=True
            elif p1[1]<=s and ldown:
                times+=1
                ldown=False
                rdown=True
        #distanceCM=int(round(A*distance**2+B*distance+C,0))
    cv2.imshow("video",img)
    key=cv2.waitKey(1)
    if  key == ord('q'):
            break
    elif key == ord('a'):
        hipy=lmList_p[24][1]
        kneey=lmList_p[26][1]
        s=int((hipy+kneey)/2)
        print(f"{s}")
        d=True
        rdown=True
        ldown=True
    elif key == ord('s'):
        times=0
        continue
cap.release()
cv2.destroyAllWindows()
