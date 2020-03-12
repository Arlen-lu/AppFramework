import os
import sys
sys.path.append(os.getcwd())
from Common.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as MB
class BottomWidget(BasePage):

    def __init__(self,driver,logging,model=None):
        super(BottomWidget,self).__init__(driver,logging)
        self.driver = driver
        self.logging= logging
        # self.model = model

    def switch_bottom_widget(self,name):
        self.logging.info('切换到页面{}'.format(name))
        loc = (MB.ANDROID_UIAUTOMATOR,'new UiSelector().text("{}")'.format(name))
        self.visiable_ele(loc)
        self.click_ele(loc)

    def visiable_bottom_widget(self,name):
        loc = (MB.ANDROID_UIAUTOMATOR,'new UiSelector().text("{}")'.format(name))
        return self.judge_visiable_ele(loc)


