from tkinter import *
import cv2
import math
import time
import cvzone
from cvzone.PoseModule import PoseDetector
from PIL import Image,ImageTk
import pygame
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database"
)
c = conn.cursor()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("voice.mp3")
cap1=cv2.VideoCapture(0)
cap1.set(3,1280)
cap1.set(4,720)
cap2=cv2.VideoCapture(1)
cap2.set(3,1280)
cap2.set(4,720)
root=Tk()
root.title("opcncv+tkinter")
#width = 2560
#height = 1500
#left = 0
#top = 0
#root.geometry(f'{width}x{height}+{left}+{top}')
detector_p= PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)
level=[9,8,7.58,7.2,6.86,6.55,6.26,6,5.76,5.54,5.33,5.14,4.97,4.8,4.65,4.5,4.36,4.24,4.11,4,3.89]
round=[7,15,23,32,41,51,61,72,83,94,106,118,131,144,157,171,185,200,215,231,247]
def a():
    global r
    global start
    global lv
    global fail
    global begin
    global delay
    start=time.time()
    lv=1
    r=0
    fail=0
    delay=0
    begin=True
    pygame.mixer.music.play(1,9)

def s():
    global begin
    global id
    begin=False
    print("round:",r)
    print("fail:",fail)
    pygame.mixer.music.stop()
    c.execute(f"INSERT INTO game_data (id,r) VALUES ({id},{r})")
    conn.commit()
    id+=1
    
start=time.time()
goal=False
begin=False
lv=1
r=0
fail=0
delay=0
id=1
def video_loop():
    global r
    global fail
    global lv
    global goal
    global start
    global begin
    global delay
    goal=False
    ran=True
    end=time.time()
    times=math.floor((end-start+delay)*100)/100
    success1,img1=cap1.read()
    img1=cv2.resize(img1,(640,360))
    success2,img2=cap2.read()
    img2=cv2.resize(img2,(640,360))
    if success1:
        cv2.line(img1,(140,200),(530,200),(0,0,255),5)
        pose=detector_p.findPose(img1)
        lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
        if times>=level[lv-1] and begin and r%2==0 and ran:
            ran=FALSE
            delay=times-level[lv-1]
            if lmList_p:
                y1=lmList_p[32][1]
                y2=lmList_p[31][1]
                p1=y1
                p2=y2
                if p1>200 and p2>200:
                    goal=True
                else:
                    goal=False
            if goal:
                r+=1
            else:
                r+=1
                fail+=1
            print(times,delay)
            start=time.time()
        cvzone.putTextRect(img1,f"round:{r}",(50,50),2.1)
        cvzone.putTextRect(img1,f"fail:{fail}",(550,150),2.1)
        cvzone.putTextRect(img1,f"{times}s",(550,50),2.1)
        cv2image1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGBA)
        current_image1=Image.fromarray(cv2image1)
        imgtk1=ImageTk.PhotoImage(image=current_image1)
        panel1.imgtk=imgtk1
        panel1.config(image=imgtk1)
        
    if success2:
        pose=detector_p.findPose(img2)
        cv2.line(img2,(140,200),(530,200),(0,0,255),5)
        lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
        if times>=level[lv-1] and begin and r%2==1 and ran:
            delay=times-level[lv-1]
            ran=False
            if lmList_p:
                y1=lmList_p[32][1]
                y2=lmList_p[31][1]
                p1=y1
                p2=y2
                if p1>200 and p2>200:
                    goal=True
                else:
                    goal=False
            if goal:
                r+=1
            else:
                r+=1
                fail+=1
            print(times,delay)
            start=time.time()
        cvzone.putTextRect(img2,f"round:{r}",(50,50),2.1)
        cvzone.putTextRect(img2,f"fail:{fail}",(550,150),2.1)
        cvzone.putTextRect(img2,f"{times}s",(550,50),2.1)
        cv2image2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGBA)
        current_image2=Image.fromarray(cv2image2)
        imgtk2=ImageTk.PhotoImage(image=current_image2)
        panel2.imgtk=imgtk2
        panel2.config(image=imgtk2)
        
    if r==round[lv-1]:
            lv+=1
    if lv>21:
        begin=False
    """
    if fail==2 and begin:
        begin=False
        c.execute(f"INSERT INTO game_data (id,r) VALUES ({id},{r})")
        conn.commit()
        pygame.mixer.music.stop()
        id+=1
    """
    root.after(1,video_loop) #每隔1毫秒執行一次 video_roop 函式

panel1=Label(root) #initialize image panel
panel1.pack(side="top")
panel2=Label(root) #initialize image panel
panel2.pack(side="top")
root.config(cursor="arrow")
btna=Button(root,text="開始",command=a)
btna.pack(fill="x",expand=True,side="left")
btns=Button(root,text="結束",command=s)
btns.pack(fill="x",expand=True,side="right")
video_loop()
root.mainloop()
cap1.release()
cap2.release()
conn.close()