# 匯入函式庫
import cv2 
import numpy as np

# 讀取圖片
img = cv2.imread('Picture.png')

# OpenCV的顏色預設是BGR格式，這邊將其轉換為HSV格式
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 以HSV格式決定要提取的顏色範圍，顏色格式的說明請參考後續內容
lower = np.array([100,43,46])
upper = np.array([124,255,255])
# 將HSV影像的閾值設定為想要提取的顏色
mask = cv2.inRange(hsv, lower, upper)
# 使用bitwise_and()合併掩膜(mask)和原來的影像
img_specific = cv2.bitwise_and(img,img, mask= mask)
# 存檔
cv2.imwrite('img_specific.jpg', img_specific)
# 展示原圖、掩膜、抽取顏色後的影像
cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow(' img_specific ', img_specific)
cv2.waitKey(0)
cv2.destroyAllWindows()
