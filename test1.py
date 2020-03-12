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
desired_caps['appActivity'] = ".WebViewBrowserActivity"
desired_caps['appPackage'] = "org.chromium.webview_shell"
desired_caps['noReset'] ="true"
desired_caps['automationName'] = "UiAutomator2"   #为了读取到toast

#adb shell dumpsys activity activities | grep "Run"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(10)
size = driver.get_window_size()
width = size['width']
height = size['height']
driver.swipe(width/2,height*0.1,width/2,height*0.9,duration=2000)
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'org.chromium.webview_shell:id/url_field')))
driver.find_element_by_id('org.chromium.webview_shell:id/url_field').send_keys('http://www.baidu.com')
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID,'Load URL')))
driver.find_element_by_accessibility_id('Load URL').click()
driver.find_element_by_accessibility_id('Load URL').get_attribute()
activity = driver.current_activity
print(activity)
contexts = driver.contexts
print(contexts)
# driver.switch_to.context('WEBVIEW_org.chromium.webview_shell')  #切换到html亚眠
#切换回NATIVE_APP 页面
# driver.switch_to.context(None)
# locator = (MobileBy.ID,'index-kw')
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
# driver.find_element_by_id('index-kw').send_keys('微信')
# driver.find_element_by_id('index-bn').click()
# locator = (MobileBy.XPATH,"//h3[contains(@class,'c-title-label')]/span[@class='c-title-text']")
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
# ele = driver.find_element_by_xpath("//h3[contains(@class,'c-title-label')]/span[@class='c-title-text']")
# driver.execute_script('arguments[0].scrollIntoView();',ele)
# time.sleep(2)
# ele.click()
# locator=(MobileBy.ID,'btn_menu_download')
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
# ele = driver.find_element_by_id('btn_menu_download')
# ele.click()
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'androidDownloadBtn')))
# driver.find_element_by_id('androidDownloadBtn').click()
# driver.close_app()
# driver.quit()