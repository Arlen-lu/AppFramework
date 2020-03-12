import os
import sys
base_path = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.split(base_path)[0])
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import logging
from Common import dir_config
import time
import os
import subprocess



class BasePage(object):

    def __init__(self,driver,logging,model = None):
        '''
        param:model case name
        '''
        self.driver = driver
        self.model = model
        self.logging = logging

    #确认元素是否出现
    def visiable_ele(self,loc,timeout = 20,poll_frequency=0.01):
        '''
        - driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
        - timeout - Number of seconds before timing out
        - poll_frequency - sleep interval between calls
        '''
        try:
            start_t = time.time()
            WebDriverWait(self.driver,timeout=20,poll_frequency=0.01).until(EC.visibility_of_element_located(loc))
            end_t = time.time()
            logging.info('元素{0}查找成功，耗时{1}s'.format(loc,(end_t-start_t)))
        except Exception as e:
            self.imgs_screenshot()
            logging.exception("元素{0}未找到".format(loc))
            raise e
    #判定是否存在
    def judge_visiable_ele(self,loc,timeout = 2,poll_frequency=0.01):
        try:
            WebDriverWait(self.driver,timeout=2,poll_frequency=0.01).until(EC.visibility_of_element_located(loc))
            return True
        except:
            return False
    #判定toast是否存在
    def is_toast_exists(self,loc):
        try:
            ele = WebDriverWait(self.driver,timeout=10,poll_frequency=0.01).until(EC.presence_of_element_located(loc))
            return ele.text
            logging.info('读取到toast元素{}得text值'.format(loc))
        except Exception as e:
            logging.info('未读取到toast元素{}得text值'.format(loc))
            raise e

     #定位元素
    def get_ele(self,loc):
        self.visiable_ele(loc)
        try:
            ele = self.driver.find_element(*loc)
            logging.info('元素{}查找成功！'.format(loc))
            return ele
        except Exception as e:
            self.imgs_screenshot()
            logging.exception("元素{0}查找失败！".format(loc))
            raise e
    
    #定位到多个元素
    def get_eles(self,loc):
        try:
            eles = self.driver.find_elements(*loc)
            logging.info('元素集合{}查找成功!'.format(loc))
            return eles
        except Exception as e:
            logging.exception("元素集合{}查找失败".format(loc))
            raise e
    # #元素是否可点击
    # def is_clickable(self,ele):
    #     return ele.is_enabled()
    
    #输入
    def input_ele_text(self,loc,value):
        ele = self.get_ele(loc)
        try:
            ele.send_keys(value)
            logging.info('元素{0}成功输入{1}'.format(loc,value))
        except Exception as e:
            self.imgs_screenshot()
            logging.exception('元素{0}输入值{1}失败！'.format(loc,value))
            raise e
    
    #清除输入框内容
    def clear_ele_text(self,loc):
        ele = sel.get_ele(loc)
        try:
            ele.clear()
            logging.info('成功清除元素{}得值'.format(loc))
        except Exception as e:
            self.imgs_screenshot()
            logging.exception('清除元素{0}得值失败！'.format(loc))
            raise e
    #click操作
    def click_ele(self,loc):
        ele = self.get_ele(loc)
        try:
            ele.click()
            logging.info('元素{0}成功点击!'.format(loc))
        except Exception as e:
            self.imgs_screenshot()
            logging.exception('元素{0}点击失败！'.format(loc))
            raise e

    #查看元素属性
    def get_ele_attr(self,loc,name):
        ele = self.get_ele(loc)
        try:
            value = ele.get_attribute(name)
            logging.info('获取元素{0}得{1}属性为{2}'.format(loc,name,value))
            return value
        except Exception as e:
            self.imgs_screenshot()
            logging.exception('获取元素{0}的{1}属性失败'.format(loc,name))
            raise e

    #封装截图
    def imgs_screenshot(self):
        #配置截图得路径和文件名称
        pic_name = '{0}-{1}.png'.format(self.model,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        pic_path = os.path.join(dir_config.dir_screen,pic_name)
        try:
            self.driver.save_screenshot(pic_path)
            logging.info('截图成功，文件为{0}'.format(pic_path))
        except Exception as e:
            logging.exception("截图失败!")
            raise e
    
    #切换上下文(NATIVE_APP与webview之间切换)  app独有
    def switch_webview(self,webview_val):
        '''
        conval:new代表切换到h5页面，其余切换到对应的页面
        '''
        #获取所有的上下文
        loc = (MobileBy.CLASS_NAME,'android.view.View')
        webdriver(self.driver,20).until(EC.visibility_of_element_located(loc))
        contexts = self.driver.contexts
        # if len(contexts) >1 and webview_val == 'new':
        if webview_val == 'new':
            try:
                self.driver.switch_to.context(contexts[-1])
                logging.info('成功切换到webview页：{}'.format(webview_val))
            except Exception as e:
                self.imgs_screenshot()
                logging.exception('切换到webview失败')
                raise e
        else:
            try:
                self.driver.switch_to.context(webview_val)
                logging.info('成功切换到wenview页：{}'.format(webview_val))
            except Exception as e:
                self.imgs_screenshot()
                logging.exception("切换失败")
                raise e
    #切换app应用，app独有
    def switch_activity(self,app_package,app_activity):
        try:
            self.driver.start_activity(app_package,app_activity)
            logging.info('成功切换到{}应用'.format(app_package))
        except Exception as e:
            self.imgs_screenshot()
            logging.exception('切换到{}应用失败！'.format(app_package))
            raise e

    #获取手机屏幕的大小
    def get_screen_size(self):
        return self.driver.get_window_size()

    #滑屏操作
    def swipe_up(self,start_y=0.1,end_y=0.9,duration = 2000):
        size = self.get_screen_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width/2,height*start_y,width/2,height*end_y,duration)

    def swipe_down(self,start_y=0.9,end_y=0.1,duration = 2000):
        size = self.get_screen_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width/2,height*start_y,width/2,height*end_y,duration)

    def swipe_left(self,start_x=0.1,end_x=0.9,duration = 2000):
        size = self.get_screen_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width*start_x,height/2,width*end_x,height/2,duration)

    def swipe_right(self,start_x=0.9,end_x=0.1,duration = 2000):
        size = self.get_screen_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width*start_x,height/2,width*end_x,height/2,duration)
    #toast
    def get_toast_text(self,part_text):
        '''text:  toast的文本信息'''
        xpath = (MobileBy.XPATH,'//*(contains(@text,part_text))')
        try:
            #等待toast元素出现
            webdriver(self.driver,20).until(EC.presence_of_element_located(xpath))
            value = self.get_ele_attr(xpath,text)
            return value
            logging.info('成功获取到toast元素{0}的text值为{1}'.format(xpath,value))
        except Exception as e:
            logging.exception('获取元素{}的text属性值失败'.format(xpath))
            self.imgs_screenshot()
            raise e
        
    
        
    #获取元素的大小、坐标
    def get_ele_size(self,loc):
        ele = self.driver.get_ele(loc)
        return ele.ele_size

    def get_ele_loc(self,loc):
        ele = self.get_ele(loc)
        return ele.location

    #按键操作 keycode
    def press_key_code(self,keycode,metastate=None,flags=None):
        self.press_keycode(keycode,metastate,flags)
    
    #隐藏键盘
    def hide_keyboard(self):
        self.driver.hide_keyboard()

    #亮屏
    def screen_light(self):
        subprocess.run(['adb','shell','input','keyevent','26'])
        # os.system('adb shell input keyevent 26')
        

   