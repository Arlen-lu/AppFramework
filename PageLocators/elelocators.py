from appium.webdriver.common.mobileby import MobileBy as MB
from selenium.webdriver.common.by import By

class IndexPageLocator(object):
    home_loginbtn_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_login')

class LoginPageLocator(object):
    #手机号码输入框
    input_tele_loc = (MB.ID,'com.xxzb.fenwoo:id/et_phone')
    #下一步按钮
    btn_next_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_next_step')
    #错误弹出框text(无效的手机号)
    popbox_prompt_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_message')
    #错误弹出框,确认按钮
    popbox_btn_confirm_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_confirm')
    #密码输入框--->错误时,text显示手机号或密码错误
    input_pwd_loc = (MB.ID,'com.xxzb.fenwoo:id/et_pwd')
    #确认按钮
    btn_confirm_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_next_step')
    #返回按钮
    btn_back_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_back')

class UserPageLocators(object):
    #弹出框,title为"设置手势密码""
    popbox_prompt_title_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_title')
    #弹出框,以后再说,推出设置手势密码
    popbox_btn_later_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_cancel')
    #弹出框,立即设置
    popbox_btn_set_lock_loc =(MB.ID,'com.xxzb.fenwoo:id/btn_confirm')
    #用户名称
    user_name_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_name')
    #余额
    remain_balance_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_name')
    #安全中心按钮
    btn_safety_center_loc = (MB.ID,'com.xxzb.fenwoo:id/textView11')
    #设置i按钮
    btn_user_setting_loc = (MB.ID,'com.xxzb.fenwoo:id/iv_switch_slider')
    #进入用户中心得按钮
    btn_user_info_loc = (MB.ID,'com.xxzb.fenwoo:id/iv_user_info')
    #用户头像,为pic
    btn_user_info_pic_loc = (MB.ID,'com.xxzb.fenwoo:id/iv_head')
    #用户名称
    user_info_name_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_nick')

class ProjectsPageLocators(object):
    #定位可投标得标的列表
    projects_list_loc = (MB.ID,'com.xxzb.fenwoo:id/pbar_process')
    #标的已投的比例,判定是否可投资,"已完成"
    details_remain_percent_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_remaintime')
    #标的剩余有效期,
    details_remain_time_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_bidremain')
    #标的总额
    details_total_money_num_loc =(MB.ID,'com.xxzb.fenwoo:id/tv_amount')
    #标的总额单位(万,千万)
    details_total_money_unit_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_amountunit')
    #用户可用余额,可查看,可输入,清除输入的数字,再查看投资后的余额
    details_input_remain_money_loc = (MB.ID,'com.xxzb.fenwoo:id/et_investamount')
    #立即投标
    btn_details_invest_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_investnow')
    #返回按钮
    btn_back_invest_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_back')

    #toast
    #输入金额为0
    details_toast_0_loc = (MB.XPATH,"//*[@text='最小投资金额为:100.0']")
    #输入金额不为100倍数
    details_toast_1_loc = (MB.XPATH,"//*[@text='投资金额必须为100的整数倍']")
    #输入金额超出标的总额/超出用户余额
    details_toast_2_loc = (MB.XPATH,"//*[contains(@text,'最大投资金额为')]")
    details_toast_loc = (MB.XPATH,"//*[contains(@text,'投资金额')]")
    
    # details_toast_3_loc = (MB.XPATH,"//*[contains(@text,'最大投资金额为:']")
    #投资成功弹出框提示信息
    popbox_invest_success_loc = (MB.ID,'com.xxzb.fenwoo:id/tv_title')
    #确认按钮
    popbox_invest_confirm_loc = (MB.ID,'com.xxzb.fenwoo:id/btn_confirm')


    



    