'''
conftest:fixture 
仅适用于同一/下一目录层级
'''
import os
import sys
base_path = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]
sys.path.append(base_path)
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import pytest
import time
from Caps.getcaps import GetCaps
from Common.logger import logging


def pytest_configure(config):
    mark_list = ['test','smoke','testinvest','testlogin']
    for markers in mark_list:
        config.addinivalue_line(
            "markers", markers
        )



# noReset:True / False  重置app状态,决定初始页面是否是欢迎页面
#默认情况,noRest=false,automationName=appium
def base_driver(automationName=None,noReset=None):
    descired_caps = GetCaps().get_caps()[0]
    server_port = GetCaps().get_caps()[1]
    if automationName is not None:
        descired_caps['automationName']=automationName
    if noReset is not None:
        descired_caps['noReset'] = noReset
    driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(server_port),descired_caps)
    return driver

#欢迎页面处理(每次打开模拟器,都需要判定)
def swipe_welcome(driver):
    activity = driver.current_activity
    size = driver.get_window_size()
    if 'MainActivity' not in activity:
        for i in range(0,4):
            driver.flick(size['width']*0.9,size['height']*0.3,size['width']*0.1,size['height']*0.3)
        #点击[立即体验],进入app应用首页
        # time.sleep(1)
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Button")')))
        driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()
        time.sleep(2)
 #屏幕解锁,滑屏
# def unlock_screen(driver):
#         size = driver.get_window_size()
#         width = size['width']
#         height = size['height']
#         time.sleep(2)
#         driver.swipe(width/2,height*0.1,width/2,height*0.9,duration=2000)
#         time.sleep(2)

@pytest.fixture(scope='session')
def init_session():
    # driver = base_driver()
    # unlock_screen(driver)
    logging.info("xxxxxxx")
    yield logging

@pytest.fixture(scope='class')
def init_class_keep():
    driver = base_driver(automationName=None,noReset=True)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()

@pytest.fixture(scope='class')
def init_class_keep_toast():
    driver = base_driver(automationName='UIAutomator2',noReset=True)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()

@pytest.fixture(scope='class')
def init_class_reset():
    driver = base_driver(automationName=None,noReset=False)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()
@pytest.fixture(scope='class')
def init_class_reset_toast():
    driver = base_driver(automationName='UIAutomator2',noReset=False)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()


#清除app应用数据
@pytest.fixture()
def init_reset_toast():
    driver = base_driver(automationName='UIAutomator2',noReset=False)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()

#不清除app数据
@pytest.fixture()
def init_keep():
    driver = base_driver(automationName=None,noReset=True)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()

#toast判定,要求:automationName需要指定为UiAutomator2
@pytest.fixture()#默认function
def init_toast_reset():
    driver = base_driver(automationName='UiAutomator2',noReset=False)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()

@pytest.fixture()#默认function
def init_toast_keep():
    driver = base_driver(automationName='UiAutomator2',noReset=True)
    time.sleep(2)
    swipe_welcome(driver)
    yield driver
    driver.close_app()
    driver.quit()


        




