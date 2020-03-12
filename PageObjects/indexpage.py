import os
import sys
sys.path.append(os.getcwd())
from Common.basepage import BasePage
from PageLocators.elelocators import IndexPageLocator as loc
from PageObjects.bottom_widget import BottomWidget
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#首页
class IndexPage(BasePage):

    def __init__(self,driver,logging,model):
        super(IndexPage,self).__init__(driver,logging,model)
        self.driver = driver
        self.model = model
        self.logging = logging

    def visiable_login_btn(self):
        time.sleep(2)
        BottomWidget(self.driver,self.logging,self.model).switch_bottom_widget('首页')
        return self.judge_visiable_ele(loc.home_loginbtn_loc)
