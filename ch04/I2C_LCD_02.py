# 匯入I2C_LCD_driver函式庫
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()
# 在第2列, 第3行的位置顯示字串Jetson Nano 
mylcd.lcd_display_string("Jetson Nano", 2,3)
