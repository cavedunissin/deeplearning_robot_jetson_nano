import cv2
import numpy as np
# 讀取影像
img_gray = cv2.imread('img_gray.jpg')
img_specific = cv2.imread('img_specific.jpg')

# 將提取顏色的影像轉換為灰階
img_specific_gray = cv2.cvtColor(img_specific,cv2.COLOR_BGR2GRAY)     
# 下方數字50為閾值，可修改閾值範圍(0~255)來調整掩膜區域，並轉換為二元影像
ret, mask = cv2.threshold(img_specific_gray,50, 255, cv2.THRESH_BINARY)
# 將掩膜反相
mask_inv = cv2.bitwise_not(mask)

# 使用bitwise_and()和掩膜從灰階圖中排除已被提取顏色的區域
img_gray_bg = cv2.bitwise_and(img_gray,img_gray,mask = mask_inv)
# 使用bitwise_and()和掩膜設定提取顏色的區域
img_specific_fg = cv2.bitwise_and(img_specific,img_specific,mask = mask)

# 使用add()將兩張圖片疊加
img_result = cv2.add(img_gray_bg,img_specific_fg)
# 存檔並展示
cv2.imwrite(' img_result.jpg', img_result)
cv2.imshow(' img_result ', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
