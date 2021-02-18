# 匯入函式庫
import cv2
import numpy as np

# 讀取影像
img = cv2.imread('Picture.png')
# 將影像轉換為灰階
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
# 存檔
cv2.imwrite('img_gray.jpg',img_gray)
# 開啟視窗顯示影像
cv2.imshow('img_gray',img_gray)
# 不刷新影像
cv2.waitKey(0)
# 釋放資源
cv2.destroyAllWindows()
