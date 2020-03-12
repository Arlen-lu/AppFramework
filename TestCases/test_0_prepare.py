import os
import sys
sys.path.append(os.getcwd())
from PageObjects.indexpage import IndexPage
import pytest

@pytest.mark.usefixtures('init_session')
@pytest.mark.usefixtures('init_class_reset')
class TestPreprae(object):

    #初始化操作,先确认app是否已登录
    @pytest.mark.testlogin
    def test_prepare(self,init_class_reset,init_session):
        name = '测试准备,清除应用数据'
        try:
            IndexPage(init_class_reset,init_session,name).visiable_login_btn()
            init_session.info('app未登录,开始执行用例!')
        except:
            init_session.info('app已登录,执行数据清空操作!') 