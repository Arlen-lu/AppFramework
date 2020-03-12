import os
import sys
sys.path.append(os.getcwd())
from PageObjects.projectspage import ProjectsPage
from PageObjects.bottom_widget import BottomWidget
from PageObjects.indexpage import IndexPage
from PageObjects.loginpage import LoginPage
from PageObjects.userpage import UserPage
from TestDatas.gettestdatas import GetTestDatas
import time
# from TestCases.test_0_login import TestLogin
import pytest

# @pytest.mark.testinvest
@pytest.mark.usefixtures('init_session')
@pytest.mark.usefixtures('init_class_keep_toast')
class TestInvest(object):

    def prepare_login(self,driver,logging,name,testdatas):
        logging.info('前提:登录状态')
        BottomWidget(driver,logging,name).switch_bottom_widget('我')
        LoginPage(driver,logging,name).input_tele(testdatas['tele'])
        LoginPage(driver,logging,name).input_pwd(testdatas['pwd'])
        time.sleep(2)
        if UserPage(driver,logging,name).popbox_is_visiable():
            UserPage(driver,logging,name).click_popbox_btn_later()
        time.sleep(2)
        try:
            assert not IndexPage(driver,logging,name).visiable_login_btn()
            logging.info('确认登录成功!')
        except Exception as e:
            logging.exception('登录失败!')
            raise e


    @pytest.mark.testinvest
    @pytest.mark.parametrize('testdatas',GetTestDatas().get_testdatas()['invest_wrong'])
    @pytest.mark.parametrize('logindata',GetTestDatas().get_testdatas()['login_success'])
    def test_invest_worng(self,init_class_keep_toast,init_session,testdatas,logindata):
        '''
        前提:已登录状态
        1.进入到"项目"页签
        2.点击可投资的项目
        3.输入投资金额
        4.点击投标按钮
        5.确认toast错误提示
        '''
        name = '投标操作'
        #判定是否已登录,若未登录,则执行登录操作
        if IndexPage(init_class_keep_toast,init_session,name).visiable_login_btn():
            init_session.info('app处于未登录状态,进行账号登录!')
            name1 = '前提:登录状态'
            self.prepare_login(init_class_keep_toast,init_session,name1,logindata)
        if BottomWidget(init_class_keep_toast,init_session,name).visiable_bottom_widget('项目'):
            BottomWidget(init_class_keep_toast,init_session,name).switch_bottom_widget('项目')
            ProjectsPage(init_class_keep_toast,init_session,name).ensure_invest_is_visiable()
        remain_money = ProjectsPage(init_class_keep_toast,init_session,name).get_details_input_remain_money()
        init_session.info('用户剩余金额{}'.format(remain_money))
        ProjectsPage(init_class_keep_toast,init_session,name).input_details_input_remain_money(testdatas['ammount'])
        ProjectsPage(init_class_keep_toast,init_session,name).click_btn_details_invest()
        toast_text = ProjectsPage(init_class_keep_toast,init_session,name).visiable_toast()
        init_session.info('toast信息显示为{}'.format(toast_text))
        try:
            if testdatas['ammount'] ==0:
                assert toast_text ==testdatas['msg']
                init_session.info('Test Pass!')
            elif testdatas['ammount']%100 !=0:
                assert toast_text ==testdatas['msg']
                init_session.info('Test Pass!')
            elif testdatas['ammount'] >remain_money or testdatas['ammount']>ProjectsPage(init_class_keep_toast,init_session,name).get_details_invest_balance():
                assert testdatas['msg'] in toast_text
                init_session.info('Test Pass!')
        except Exception as e:
            init_session.exception('Test Fail!')
            raise e
        finally:
            ProjectsPage(init_class_keep_toast,init_session,name).btn_back()

    # @pytest.mark.testinvest
    @pytest.mark.parametrize('testdatas',GetTestDatas().get_testdatas()['invest_success'])
    @pytest.mark.parametrize('logindata',GetTestDatas().get_testdatas()['login_success'])
    # @pytest.mark.usefixtures('init_keep')
    def test_invest_success(self,init_class_keep_toast,init_session,testdatas,logindata):
        '''
        前提:已登录状态
        1.进入到"项目"页签
        2.点击可投资的项目
        3.输入投资金额
        4.点击投标按钮
        5.确认投资成功(投资成功+资金变化)
        '''
        #判定是否已登录,若未登录,则执行登录操作
        name = '投标操作'
        if IndexPage(init_class_keep_toast,init_session,name).visiable_login_btn():
            init_session.info('app处于未登录状态,进行账号登录!')
            name1 = '前提:登录状态'
            self.prepare_login(init_class_keep_toast,init_session,name1,logindata)
        BottomWidget(init_class_keep_toast,init_session,name).switch_bottom_widget('项目')
        ProjectsPage(init_class_keep_toast,init_session,name).ensure_invest_is_visiable()
        ProjectsPage(init_class_keep_toast,init_session,name).input_details_input_remain_money(testdatas['ammount'])
        ProjectsPage(init_class_keep_toast,init_session,name).click_btn_details_invest()
        try:
            assert ProjectsPage(init_class_keep_toast,init_session,name).get_popbox_invest_success() ==testdatas['msg']
            init_session.info('投资成功!')
        except Exception as e:
            init_session.exception('投资失败!')
            raise e
        else:
            ProjectsPage(init_class_keep_toast,init_session,name).click_popbox_invest_confirm()

