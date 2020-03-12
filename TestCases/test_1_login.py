import os
import sys
sys.path.append(os.getcwd())
import pytest
import time
from PageObjects.indexpage import IndexPage
from PageObjects.bottom_widget import BottomWidget
from PageObjects.loginpage import LoginPage
from TestDatas.gettestdatas import GetTestDatas
from PageObjects.userpage import UserPage
@pytest.mark.testlogin
@pytest.mark.usefixtures('init_session')
class TestLogin(object):

    # @pytest.mark.test
    @pytest.mark.parametrize('testdatas',GetTestDatas().get_testdatas()['login_tele_wrong'])
    @pytest.mark.usefixtures('init_class_keep')
    def test_login_tele_wrong(self,init_class_keep,init_session,testdatas):
        init_session.info('手机号输入错误用例')
        name = '手机号输入错误'
        if BottomWidget(init_class_keep,init_session,name).visiable_bottom_widget('我'):
            BottomWidget(init_class_keep,init_session,name).switch_bottom_widget('我')
        LoginPage(init_class_keep,init_session,name).input_tele(testdatas['tele'])
        time.sleep(2)
        try:
            assert LoginPage(init_class_keep,init_session,name).get_popbox_text() == testdatas['msg']
            init_session.info('Test Pass!')
        except Exception as e:
            init_session.info('Test Fail')
            raise e
        finally:
            LoginPage(init_class_keep,init_session,name).popbox_prompt_btn()

    # @pytest.mark.test
    @pytest.mark.parametrize('testdatas',GetTestDatas().get_testdatas()['login_success'])
    @pytest.mark.usefixtures('init_keep')
    def test_login_success(self,init_class_keep,init_session,testdatas):
        init_session.info('成功登录用例')
        name = '成功登录'
        BottomWidget(init_class_keep,init_session,name).switch_bottom_widget('我')
        LoginPage(init_class_keep,init_session,name).input_tele(testdatas['tele'])
        LoginPage(init_class_keep,init_session,name).input_pwd(testdatas['pwd'])
        time.sleep(2)
        if UserPage(init_class_keep,init_session,name).popbox_is_visiable():
            UserPage(init_class_keep,init_session,name).click_popbox_btn_later()
        time.sleep(2)
        # BottomWidget(init_keep,init_session,name).switch_bottom_widget('首页')
        try:
            assert not IndexPage(init_class_keep,init_session,name).visiable_login_btn()
            init_session.info('确认登录成功!')
        except Exception as e:
            init_session.exception('登录失败!')
            raise e


        

        

