import cv2
import numpy as np

def calculate_distance(point1, point2, pixel_to_distance_ratio):
    # 計算兩點之間的歐幾里得距離
    distance_pixels = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    # 將像素距離轉換為實際距離
    distance_real = distance_pixels * pixel_to_distance_ratio
    return distance_real

def draw_circle(event, x, y, flags, param):
    global mouseX, mouseY, point1, point2
    if event == cv2.EVENT_LBUTTONDOWN:
        if point1 is None:
            point1 = (x, y)
            print(point1)
        elif point2 is None:
            point2 = (x, y)
            print(point2)
            # 當選擇了兩個點後，計算距離並顯示結果
            distance = calculate_distance(point1, point2, pixel_to_distance_ratio)
            print("距離：", distance, "單位")

# 讀取圖片
image = cv2.imread('environment.png')
# 設置實際距離和像素之間的比例，例如每像素代表實際距離的1個單位
pixel_to_distance_ratio = 0.16120647005

# 創建一個空窗口並綁定鼠標事件
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

point1 = None
point2 = None

while True:
    # 在圖片上標記選擇的點
    if point1:
        cv2.circle(image, point1, 5, (255, 0, 0), -1)
    if point2:
        cv2.circle(image, point2, 5, (0, 255, 0), -1)

    # 顯示圖片
    cv2.imshow('image', image)
    key = cv2.waitKey(1) & 0xFF

    # 按下 'q' 鍵退出循環
    if key == ord("q"):
        break

# 關閉所有窗口
cv2.destroyAllWindows()