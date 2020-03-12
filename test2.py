from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import subprocess
import time

desired_caps = {}
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] ="6.0.1"
desired_caps['deviceName'] = "69T7N16C02000810"
desired_caps['appActivity'] = "com.tencent.mtt.MainActivity"
desired_caps['appPackage'] = "com.android.browser"
desired_caps['noReset'] ="false" 
desired_caps['automationName'] = "Appium"
# desired_caps['unlockType'] = 'password'
# desired_caps['unlockKey'] = '1234'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
size = driver.get_window_size()
width = size['width']
height = size['height']
driver.swipe(width*0.1,height/2,width*0.9,height/2)
driver.current_activity()
driver.get_window_size
# driver.press_keycode(8)
# driver.press_keycode(9)
# driver.press_keycode(10)
# driver.press_keycode(11)
# driver.press_keycode(66)

# driver.swipe(width/2,height*0.1,width/2,height*0.9,duration=5)
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(MobileBy.ACCESSIBILITY_ID,'Device password'))
# driver.find_element_by_accessibility_id('Device password').send_keys('1234')


