import os
import sys
sys.path.append(os.getcwd())
from PageLocators.elelocators import ProjectsPageLocators as loc 
from Common.basepage import BasePage

class ProjectsPage(BasePage):

    def __init__(self,driver,logging,model=None):
        super(ProjectsPage,self).__init__(driver,logging,model)
        self.driver = driver
        self.logging = logging

    def get_projects_list(self):
        eles = self.get_eles(loc.projects_list_loc)
        return eles
    #获取标的已投百分比
    def get_details_remain_percent(self):
        return self.get_ele_attr(loc.details_remain_percent_loc,'text')
    #获取标的的剩余时间,并判定是否结束
    def get_details_remain_time(self):
        time_balance =  self.get_ele_attr(loc.details_remain_time_loc,'text')
        for i in time_balance:
            if i.isdigit() and int(i)>0:
                return True
                break
        else:
            return False

    #获取用户剩余余额
    def get_details_input_remain_money(self):
        data= self.get_ele_attr(loc.details_input_remain_money_loc,'text').replace('可用余额','').replace('元','')
        money = int(float(data))
        return money
    #输入投标的的金额
    def input_details_input_remain_money(self,value):
        self.input_ele_text(loc.details_input_remain_money_loc,value)
    #清除输入的金额
    def clear_details_input_remain_money(self):
        self.clear_ele_text(loc.details_input_remain_money_loc)
    #投标
    def click_btn_details_invest(self):
        self.click_ele(loc.btn_details_invest_loc)
    #获取成功投标的提示
    def get_popbox_invest_success(self):
        return self.get_ele_attr(loc.popbox_invest_success_loc,'text')
    #确认投标
    def click_popbox_invest_confirm(self):
        self.click_ele(loc.popbox_invest_confirm_loc)
    def ensure_invest_is_visiable(self):
        eles = self.get_projects_list()
        for ele in eles:
            ele.click()
            if self.get_details_remain_time() and self.get_details_remain_percent() != '已完成':
                self.logging.info('该标的:{}可投资'.format(ele))
                return ele
        else:
            self.logging.info('无可投资的标的')
    #输入金额为0
    def get_details_toast_0(self):
        return self.get_ele_attr(loc.details_toast_0_loc,'text')
        #输入金额不为100倍数
    def get_details_toast_1(self):
        return self.get_ele_attr(loc.details_toast_1_loc,'text')
        #输入金额超出标的总额/超出用户余额
    def get_details_toast_2(self):
        return self.get_ele_attr(loc.details_toast_2_loc,'text')
    def get_details_toast(self):
        return self.get_ele_attr(loc.details_toast_loc,'text')
    def visiable_toast(self):
        return self.is_toast_exists(loc.details_toast_loc)
    #标的得剩余金额
    def get_details_invest_balance(self):
        data = self.visiable_toast()
        money = int(float(data.split(':')[1]))
        return money
    #返回
    def btn_back(self):
        self.click_ele(loc.btn_back_invest_loc)


    
        