import os
import sys
sys.path.append(os.getcwd())
from Common.basepage import BasePage
from PageLocators.elelocators import LoginPageLocator as loc

class LoginPage(BasePage):

    def __init__(self,driver,logging,model=None):
        super(LoginPage,self).__init__(driver,logging,model)
        # self.driver = driver
        # self.logging = logging
        # self.name = model
    
    def input_tele(self,tele):
        '''输入手机号操作
        1.输入手机号
        2.点击[下一步]按钮
        '''
        self.visiable_ele(loc.input_tele_loc)
        self.input_ele_text(loc.input_tele_loc,tele)
        self.click_ele(loc.btn_next_loc)
    #获取手机号输入框的text信息
    def get_input_tele_text(self):
        return self.get_ele_attr(loc.input_tele_loc,'text')
    def clear_input_tele_text(self):
        self.clear_ele_text(loc.input_tele_loc)
    #获取错误提示框的text信息
    def get_popbox_text(self):
        return self.get_ele_attr(loc.popbox_prompt_loc,'text')
    #点击错误提示框的确认按钮,清除弹出框
    def popbox_prompt_btn(self):
        self.click_ele(loc.popbox_btn_confirm_loc)
    '''输入密码操作
    1.输入密码
    2.点击[确定]按钮
    '''
    def input_pwd(self,pwd):
        self.visiable_ele(loc.input_pwd_loc)
        self.input_ele_text(loc.input_pwd_loc,pwd)
        self.click_ele(loc.btn_confirm_loc)
    #获取密码输入框中的提示信息
    def get_input_pwd_text(self):
        return self.get_ele_attr(loc.input_pwd_loc,'text')