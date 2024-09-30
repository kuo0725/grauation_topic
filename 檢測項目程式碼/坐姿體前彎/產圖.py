#mediapipe 0.10.11
#cvaone 1.5.2
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector
import math
import numpy as np
import cvzone
import matplotlib.pyplot as plt
import time
cap=cv2.VideoCapture("15a.mp4")
cap.set(3,1280)
cap.set(4,720)
detector_p= PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
detector_h=HandDetector(detectionCon=0.9,maxHands=1,minTrackCon=0.9)
dx=[32,56,82,112,141,175,210,248,286,328,378,425]
dy=[5,10,15,20,25,30,35,40,45,50,55,60]
coff=np.polyfit(dx,dy,2) #y=Ax^2+Bx+C
A,B,C=coff
p1=[397,731,-25]
landmarks_p=[]
lmList_h=[]
def skeleton(lmList_p,lmList_h,cm):
    fig=plt.figure(figsize=(10,10))
    ax = plt.subplot(projection='3d')
    ax.set_zticks([])
    eyex=[lmList_p[8][0],lmList_p[6][0],lmList_p[5][0],lmList_p[4][0],lmList_p[0][0],lmList_p[1][0],lmList_p[2][0],lmList_p[3][0],lmList_p[7][0]]
    eyey=[lmList_p[8][1],lmList_p[6][1],lmList_p[5][1],lmList_p[4][1],lmList_p[0][1],lmList_p[1][1],lmList_p[2][1],lmList_p[3][1],lmList_p[7][1]]
    eyez=[lmList_p[8][2],lmList_p[6][2],lmList_p[5][2],lmList_p[4][2],lmList_p[0][2],lmList_p[1][2],lmList_p[2][2],lmList_p[3][2],lmList_p[7][2]]
    mouthx=[lmList_p[9][0],lmList_p[10][0]]
    mouthy=[lmList_p[9][1],lmList_p[10][1]]
    mouthz=[lmList_p[9][2],lmList_p[10][2]]
    handtx=[lmList_p[12][0],lmList_p[14][0],lmList_h[0][0],lmList_h[1][0],lmList_h[2][0],lmList_h[3][0],lmList_h[4][0],lmList_h[3][0],lmList_h[2][0],lmList_h[1][0],lmList_h[0][0],lmList_h[5][0],lmList_h[9][0],lmList_h[13][0],lmList_h[17][0],lmList_h[0][0],lmList_p[13][0],lmList_p[11][0]]
    handty=[lmList_p[12][1],lmList_p[14][1],lmList_h[0][1],lmList_h[1][1],lmList_h[2][1],lmList_h[3][1],lmList_h[4][1],lmList_h[3][1],lmList_h[2][1],lmList_h[1][1],lmList_h[0][1],lmList_h[5][1],lmList_h[9][1],lmList_h[13][1],lmList_h[17][1],lmList_h[0][1],lmList_p[13][1],lmList_p[11][1]]
    handtz=[lmList_p[12][2],lmList_p[14][2],lmList_h[0][2],lmList_h[1][2],lmList_h[2][2],lmList_h[3][2],lmList_h[4][2],lmList_h[3][2],lmList_h[2][2],lmList_h[1][2],lmList_h[0][2],lmList_h[5][2],lmList_h[9][2],lmList_h[13][2],lmList_h[17][2],lmList_h[0][2],lmList_p[13][2],lmList_p[11][2]]
    handfx=[lmList_h[5][0],lmList_h[6][0],lmList_h[7][0],lmList_h[8][0]]
    handfy=[lmList_h[5][1],lmList_h[6][1],lmList_h[7][1],lmList_h[8][1]]
    handfz=[lmList_h[5][2],lmList_h[6][2],lmList_h[7][2],lmList_h[8][2]]
    handmx=[lmList_h[9][0],lmList_h[10][0],lmList_h[11][0],lmList_h[12][0]]
    handmy=[lmList_h[9][1],lmList_h[10][1],lmList_h[11][1],lmList_h[12][1]]
    handmz=[lmList_h[9][2],lmList_h[10][2],lmList_h[11][2],lmList_h[12][2]]
    handrx=[lmList_h[13][0],lmList_h[14][0],lmList_h[15][0],lmList_h[16][0]]
    handry=[lmList_h[13][1],lmList_h[14][1],lmList_h[15][1],lmList_h[16][1]]
    handrz=[lmList_h[13][2],lmList_h[14][2],lmList_h[15][2],lmList_h[16][2]]
    handpx=[lmList_h[17][0],lmList_h[18][0],lmList_h[19][0],lmList_h[20][0]]
    handpy=[lmList_h[17][1],lmList_h[18][1],lmList_h[19][1],lmList_h[20][1]]
    handpz=[lmList_h[17][2],lmList_h[18][2],lmList_h[19][2],lmList_h[20][2]]
    bodyx=[lmList_p[12][0],lmList_p[11][0],lmList_p[23][0],lmList_p[24][0],lmList_p[12][0]]
    bodyy=[lmList_p[12][1],lmList_p[11][1],lmList_p[23][1],lmList_p[24][1],lmList_p[12][1]]
    bodyz=[lmList_p[12][2],lmList_p[11][2],lmList_p[23][2],lmList_p[24][2],lmList_p[12][2]]
    legrx=[lmList_p[28][0],lmList_p[30][0],lmList_p[32][0],lmList_p[28][0],lmList_p[26][0],lmList_p[24][0]]
    legry=[lmList_p[28][1],lmList_p[30][1],lmList_p[32][1],lmList_p[28][1],lmList_p[26][1],lmList_p[24][1]]
    legrz=[lmList_p[28][2],lmList_p[30][2],lmList_p[32][2],lmList_p[28][2],lmList_p[26][2],lmList_p[24][2]]
    leglx=[lmList_p[27][0],lmList_p[31][0],lmList_p[29][0],lmList_p[27][0],lmList_p[25][0],lmList_p[23][0]]
    legly=[lmList_p[27][1],lmList_p[31][1],lmList_p[29][1],lmList_p[27][1],lmList_p[25][1],lmList_p[23][1]]
    leglz=[lmList_p[27][2],lmList_p[31][2],lmList_p[29][2],lmList_p[27][2],lmList_p[25][2],lmList_p[23][2]]
    ax.plot(eyex,eyey,eyez,color='#f90')
    ax.scatter(eyex,eyey,eyez,s=90)
    ax.plot(mouthx,mouthy,mouthz,color='#f90')
    ax.scatter(mouthx,mouthy,mouthz,s=90)
    ax.plot(handtx,handty,handtz,color='#f90')
    ax.scatter(handtx,handty,handtz,s=90)
    ax.plot(handfx,handfy,handfz,color='#f90')
    ax.scatter(handfx,handfy,handfz,s=90)
    ax.plot(handmx,handmy,handmz,color='#f90')
    ax.scatter(handmx,handmy,handmz,s=90)
    ax.plot(handrx,handry,handrz,color='#f90')
    ax.scatter(handrx,handry,handrz,s=90)
    ax.plot(handpx,handpy,handpz,color='#f90')
    ax.scatter(handpx,handpy,handpz,s=90)
    ax.plot(bodyx,bodyy,bodyz,color='#f90')
    ax.scatter(bodyx,bodyy,bodyz,s=90)
    ax.plot(legrx,legry,legrz,color='#f90b')
    ax.scatter(legrx,legry,legrz,s=90)
    ax.plot(leglx,legly,leglz,color='#f90')
    ax.scatter(leglx,legly,leglz,s=90)
    #ax.text(lmList_h[12][0]+10,lmList_h[12][1]+10,lmList_h[12][2],cm)
    ax.view_init(-90,180,90)#上下，左右
    plt.show()
    plt.close()
while True:
    success,img=cap.read()
    if not success:
        break
    pose=detector_p.findPose(img,draw=False)
    lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
    hands=detector_h.findHands(img,draw=False)
    if len(hands[0])>0:
        lmList_h=hands[0][0]["lmList"]
        bx,by,bw,bh=hands[0][0]['bbox']
        x1,y1,z1=lmList_h[12]
        p2=[x1,y1,z1]
        distance=int(math.dist(p1,p2))
        distanceCM=int(round(A*distance**2+B*distance+C,0))
        cv2.rectangle(img,(bx,by),(bx+bw,by+bh),(255,0,255),3)
        cvzone.putTextRect(img,f"{distanceCM}CM",(bx+5,by-10))
    cv2.imshow("video",img)
    key=cv2.waitKey(1)
    if  key == ord('q'):
            break
    elif key == ord('a'):
        p1=[x1,y1,z1]
        print(f"({x1},{y1},{z1})")
        distance=int(math.dist(p1,p2))
        distanceCM=int(round(A*distance**2+B*distance+C,0))
        skeleton(lmList_p,lmList_h,distanceCM)
    elif key == ord('s'):
        print(p2)
        print(distance)
        skeleton(lmList_p,lmList_h,distanceCM)
        print(f"{distanceCM}CM")
cap.release()
cv2.destroyAllWindows()
