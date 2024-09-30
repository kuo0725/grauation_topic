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
def skeleton(lmList_p,lmList_h,p,h,cm):
    ax.clear()
    p.extend(lmList_p)
    h.extend(lmList_h)
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

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')          # 設定影片的格式為 MJPG
out = cv2.VideoWriter('repeat.mp4', fourcc, 20.0, (width,  height))  # 產生空的影片
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
landmarks_p=[]
landmarks_h=[]
fig=plt.figure(figsize=(10,10))
ax = plt.subplot(projection='3d')
d=False
plt.ion()
while True:
    success,img=cap.read()
    if not success:
        break
    pose=detector_p.findPose(img)
    lmList_p, bboxInfo = detector_p.findPosition(pose, draw=False)
    hands=detector_h.findHands(img,draw=True)
    if len(hands[0])>0:
        lmList_h=hands[0][0]["lmList"]
        bx,by,bw,bh=hands[0][0]['bbox']
        x1,y1,z1=lmList_h[12]
        p2=[x1,y1,z1]
        distance=int(math.dist(p1,p2))
        distanceCM=int(round(A*distance**2+B*distance+C,0))
        cv2.rectangle(img,(bx,by),(bx+bw,by+bh),(255,0,255),3)
        cvzone.putTextRect(img,f"{distanceCM}CM",(bx+5,by-10))
    if d:
        out.write(img)
        skeleton(lmList_p,lmList_h,landmarks_p,landmarks_h,distanceCM)
    cv2.imshow("video",img)
    key=cv2.waitKey(1)
    if  key == ord('q'):
        print(p2)
        print(distance)
        print(f"{distanceCM}CM")
        break
    elif key == ord('a'):
        p1=[x1,y1,z1]
        d=True
        print(f"({x1},{y1},{z1})")
    elif key == ord('s'):
        print(p2)
        print(distance)
        print(f"{distanceCM}CM")
cap.release()
out.release()
cv2.destroyAllWindows()
plt.ioff()
plt.close()

fig=plt.figure(figsize=(10,10))
ax = plt.subplot(projection='3d')
x=[]
y=[]
z=[]
hx=[]
hy=[]
hz=[]
for i in landmarks_h:
    hx.append(int(i[0]))
    hy.append(int(i[1]))
    hz.append(int(i[2]))
for i in landmarks_p:
    x.append(int(i[0]))
    y.append(int(i[1]))
    z.append(int(i[2]))
n=int(len(landmarks_h)/21)
def run(data):
    ax.clear()
    ax.set_zticks([])
    eyex=[x[8+data*33],x[6+data*33],x[5+data*33],x[4+data*33],x[0+data*33],x[1+data*33],x[2+data*33],x[3+data*33],x[7+data*33]]
    eyey=[y[8+data*33],y[6+data*33],y[5+data*33],y[4+data*33],y[0+data*33],y[1+data*33],y[2+data*33],y[3+data*33],y[7+data*33]]
    eyez=[z[8+data*33],z[6+data*33],z[5+data*33],z[4+data*33],z[0+data*33],z[1+data*33],z[2+data*33],z[3+data*33],z[7+data*33]]
    mouthx=[x[9+data*33],x[10+data*33]]
    mouthy=[y[9+data*33],y[10+data*33]]
    mouthz=[z[9+data*33],z[10+data*33]]
    handtx=[x[12+data*33],x[14+data*33],hx[0+data*21],hx[1+data*21],hx[2+data*21],hx[3+data*21],hx[4+data*21],hx[3+data*21],hx[2+data*21],hx[1+data*21],hx[0+data*21],hx[5+data*21],hx[9+data*21],hx[13+data*21],hx[17+data*21],hx[0+data*21],x[13+data*33],x[11+data*33]]
    handty=[y[12+data*33],y[14+data*33],hy[0+data*21],hy[1+data*21],hy[2+data*21],hy[3+data*21],hy[4+data*21],hy[3+data*21],hy[2+data*21],hy[1+data*21],hy[0+data*21],hy[5+data*21],hy[9+data*21],hy[13+data*21],hy[17+data*21],hy[0+data*21],y[13+data*33],y[11+data*33]]
    handtz=[z[12+data*33],z[14+data*33],hz[0+data*21],hz[1+data*21],hz[2+data*21],hz[3+data*21],hz[4+data*21],hz[3+data*21],hz[2+data*21],hz[1+data*21],hz[0+data*21],hz[5+data*21],hz[9+data*21],hz[13+data*21],hz[17+data*21],hz[0+data*21],z[13+data*33],z[11+data*33]]
    handfx=[hx[5+data*21],hx[6+data*21],hx[7+data*21],hx[8+data*21]]
    handfy=[hy[5+data*21],hy[6+data*21],hy[7+data*21],hy[8+data*21]]
    handfz=[hz[5+data*21],hz[6+data*21],hz[7+data*21],hz[8+data*21]]
    handmx=[hx[9+data*21],hx[10+data*21],hx[11+data*21],hx[12+data*21]]
    handmy=[hy[9+data*21],hy[10+data*21],hy[11+data*21],hy[12+data*21]]
    handmz=[hz[9+data*21],hz[10+data*21],hz[11+data*21],hz[12+data*21]]
    handrx=[hx[13+data*21],hx[14+data*21],hx[15+data*21],hx[16+data*21]]
    handry=[hy[13+data*21],hy[14+data*21],hy[15+data*21],hy[16+data*21]]
    handrz=[hz[13+data*21],hz[14+data*21],hz[15+data*21],hz[16+data*21]]
    handpx=[hx[17+data*21],hx[18+data*21],hx[19+data*21],hx[20+data*21]]
    handpy=[hy[17+data*21],hy[18+data*21],hy[19+data*21],hy[20+data*21]]
    handpz=[hz[17+data*21],hz[18+data*21],hz[19+data*21],hz[20+data*21]]
    bodyx=[x[12+data*33],x[11+data*33],x[23+data*33],x[24+data*33],x[12+data*33]]
    bodyy=[y[12+data*33],y[11+data*33],y[23+data*33],y[24+data*33],y[12+data*33]]
    bodyz=[z[12+data*33],z[11+data*33],z[23+data*33],z[24+data*33],z[12+data*33]]
    legrx=[x[28+data*33],x[30+data*33],x[32+data*33],x[28+data*33],x[26+data*33],x[24+data*33]]
    legry=[y[28+data*33],y[30+data*33],y[32+data*33],y[28+data*33],y[26+data*33],y[24+data*33]]
    legrz=[z[28+data*33],z[30+data*33],z[32+data*33],z[28+data*33],z[26+data*33],z[24+data*33]]
    leglx=[x[27+data*33],x[31+data*33],x[29+data*33],x[27+data*33],x[25+data*33],x[23+data*33]]
    legly=[y[27+data*33],y[31+data*33],y[29+data*33],y[27+data*33],y[25+data*33],y[23+data*33]]
    leglz=[z[27+data*33],z[31+data*33],z[29+data*33],z[27+data*33],z[25+data*33],z[23+data*33]]
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
    ax.view_init(-90,180,90)#上下，左右
ani = animation.FuncAnimation(fig, run, frames=n, interval=10,repeat=False)  # 製作動畫
plt.close()
ani.save('animation.gif', fps=60,writer="pillow")