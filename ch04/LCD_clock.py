import I2C_LCD_driver
import datetime
import time
# 設定格式日期和時間的格式
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'

mylcd = I2C_LCD_driver.lcd()

while True:
    # 宣告DATE和TIME變數為從datetime函式獲取的系統時間，並指定印出格式
    DATE = datetime.datetime.now().strftime(DATE_FORMAT)
    TIME = datetime.datetime.now().strftime(TIME_FORMAT)
    # 螢幕印出日期和時間，並將格式調整為置中
    mylcd.lcd_display_string(DATE, 1,3)
    mylcd.lcd_display_string(TIME, 2,4)
    # 設定0.1秒更新一次，可修改參數自行調整畫面更新的頻率
    time.sleep(0.1)
