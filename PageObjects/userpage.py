import os
import sys
sys.path.append(os.getcwd())
from Common.basepage import BasePage
from PageLocators.elelocators import UserPageLocators as loc

class UserPage(BasePage):

    def __init__(self,driver,logging,model=None):
        super(UserPage,self).__init__(driver,logging,model)
        self.driver = driver
        self.logging = logging
        self.model = model

    def popbox_is_visiable(self):
        return self.judge_visiable_ele(loc.popbox_btn_later_loc)
    #弹出框,设置手势密码--立即设置or以后再说
    def click_popbox_btn_later(self):
        self.click_ele(loc.popbox_btn_later_loc)
    def click_popbox_btn_set_lock(self):
        self.click_ele(loc.popbox_btn_set_lock_loc)
    #获取账户名称
    def get_user_name(self):
        return self.get_ele_attr(loc.user_name_loc,'text')
    #获取账户余额
    def get_remain_balance(self):
        return self.get_ele_attr(loc.remain_balance_loc,'text')
        
    def click_btn_user_setting(self):
        self.click_ele(loc.btn_user_setting_loc)

    