from tkinter import *
import cv2
import math
import numpy as np
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector
from PIL import Image,ImageTk
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
root=Tk()
root.title("opcncv+tkinter")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')          # 設定影片的格式為 MJPG
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
p1=[418,732,-29]
r=False
def a():
    global r
    global p1
    global out
    out = cv2.VideoWriter('repeat.mp4', fourcc, 20.0, (width,  height))  # 產生空的影片
    r=True
    p1=[x1,y1,z1]
    print(f"({x1},{y1},{z1})")

def s():
    global r
    r=False
    out.release()
    print(x1,y1,z1)
    print(distance)
    print(f"{distanceCM}CM")

def video_loop():
    success,img=cap.read()
    if success:
        pose=detector_p.findPose(img)
        lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
        hands=detector_h.findHands(img,draw=True)
        if len(hands[0])>0:
            lmList_h=hands[0][0]["lmList"]
            bx,by,bw,bh=hands[0][0]['bbox']
            global x1,y1,z1,distance,distanceCM
            x1,y1,z1=lmList_h[12]
            p2=[x1,y1,z1]
            distance=int(math.dist(p1,p2))
            distanceCM=int(round(A*distance**2+B*distance+C,0))
            cv2.rectangle(img,(bx,by),(bx+bw,by+bh),(255,0,255),3)
            cvzone.putTextRect(img,f"{distanceCM}CM",(bx+5,by-10))
        if r:
            out.write(img)
        cv2image=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA)
        current_image=Image.fromarray(cv2image)
        imgtk=ImageTk.PhotoImage(image=current_image)
        panel.imgtk=imgtk
        panel.config(image=imgtk)
        root.after(1,video_loop) #每隔1毫秒執行一次 video_roop 函式

panel=Label(root) #initialize image panel
panel.pack(padx=10,pady=10)
root.config(cursor="arrow")
btna=Button(root,text="校準",command=a)
btna.pack(fill="x",expand=True,side="left")
btns=Button(root,text="紀錄成績",command=s)
btns.pack(fill="x",expand=True,side="right")
video_loop()
root.mainloop()
cap.release()