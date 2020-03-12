from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction 
import time
desired_caps = {}
#平台名称，版本
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] ="9.0"
desired_caps['deviceName'] = "Android Emulator"
desired_caps['appActivity'] = "com.lemon.lemonban.activity.WelcomeActivity"
desired_caps['appPackage'] = "com.lemon.lemonban"
desired_caps['noReset'] ="true"  #用来设置不用每次运行都安装app包
# desired_caps['app'] = "D:\Program Files (x86)\APK/lemonban_release_v2.1.2_finally.apk"  #需要安装apk得时候，需要添加app属性
desired_caps['automationName'] = "UiAutomator2" #为了读取到toast

#与appium server进行连接并发送要操作的apk信息
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.save_screenshot()
# #元素定位
# driver.find_element_by_id(com.lemon.lemonban:id/category_title)
# #UiSelector为java类，需要用java代码写
#new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")
#进入登录
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")')))
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")').click()
#等待
WebDriverWait(driver,30).until(EC.visibility_of_element_located((MobileBy.ID,'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')))
#点击头像登录
driver.find_element_by_id('com.lemon.lemonban:id/fragment_my_lemon_avatar_layout').click()
driver.tap
#获取当前正在运行的activity
current_activity = driver.current_activity
print(current_activity)
#当前页面的结构图
page_source = driver.page_source
print(page_source)

#获取当前device的配置信息
caps = driver.capabilities
device = caps.get('deviceName')
print(device)
driver.start_activity()
driver.swipe()
driver.press_keycode()
driver.keyevent()
driver.hide_keyboard()
driver.current_activity()
