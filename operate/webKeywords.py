import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from operate.searchMysql import Session
from selenium.webdriver.support.select import Select
from utils.log import Log
logger = Log()
mysqlHelper =Session(ip="106.75.147.193", user="root", passwd="Rootmperdiem@2020", db="autopus")


class WebKeywords:
    def __init__(self):
        """
        构造函数，创建driver实例
        """
        self.driver = webdriver.Chrome()

    def OpenBrowser(self,br='gc'):
        """
        打开浏览器
        :param br:gc=Google Chrome ff=firefox ie=ie
        :return:
        """
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print('not surport this browser')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def __find_element(self,locator=''):
        """
        定位元素的封装
        :param locator:
        :return:
        """
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(locator[locator.find('=') + 1:])
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(locator[locator.find('=') + 1:])
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(locator[locator.find('=') + 1:])
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_name(locator[locator.find('=') + 1:])
        elif locator.startswith('link_text='):
            ele = self.driver.find_element_by_link_text(locator[locator.find('=') + 1:])
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_partial_link_text(locator[locator.find('=') + 1:])
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_partial_link_text(locator[locator.find('=') + 1:])
        elif locator.startswith('class_name='):
            ele = self.driver.find_element_by_class_name(locator[locator.find('=') + 1:])
        else:
            ele = self.driver.find_element_by_xpath(locator)
        self.ele = ele
        return ele

    def getUrl(self,url=None):
        """
        获取URL地址打开对应地址
        :param url:
        :return:
        """
        # driver = browser()
        self.driver.get(url)


    def click(self,locator=None):
        """
        默认xpath
        :param locator:
        :return:
        """
        ele =self.__find_element(locator)
        ele.click()

    def input(self,locator=None,value=None):
        ele =self.__find_element(locator)
        ele.send_keys(str(value))

    def intoIframe(self,locator=None):
        try:
            ele = self.__find_element(locator)
            self.driver.switch_to.frame(ele)
        except Exception as e:
            logger.info(e)


    def excuteScript(self,js=None):

        """
        提供调用JavaScript方法
        :param src: 脚本文件
        :return: JavaScript脚本
        """
        return self.driver.execute_script(js)

    def quit(self):
        # self.driver = browser()
        self.driver.quit()

    def sleep(self,t=1):
        time.sleep(int(t))

    def assert_element_is_exit(self,locator=''):
        """
        断言-判断查找的元素是否存在
        :param locator:
        :return:
        """
        assert(self.__find_element(locator))

    def select_ele(self,locator=''):
        """
        定位下拉框元素查找
        :param locator:
        :return:
        """
        ele = self.__find_element(locator)
        Select(ele).select_by_index(2)

    def assert_alert_text(self,locator='', msg=None):
        """
        断言--alert弹窗文本是否符合预期效果
        :param msg:
        :return:
        """
        alert_text = self.__find_element(locator).text
        logger.logger.info(alert_text)
        assert alert_text == str(msg)

    def wait_element_visibility(self,locator=''):
        """
        等待元素出现,固定xpath,后续扩张多种定位方式
        :param locator:
        :return:
        """
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, locator)))

    def search_for_sql(self,sql):
        """
        查询数据库结果
        :param sql:
        :return:
        """
        result = mysqlHelper.query(sql)
        return result

    def move_mouse_and_double_click(self,locator=''):
        """
        滑动鼠标进行双击操作
        :param locator:
        :return:
        """
        ActionChains(self.driver).double_click(locator).perform()

    def element_is_disabled(self,locator=''):
        """
        判断元素是否可点击，属性为disabled
        :param locator:
        :return:
        """
        self.__find_element(locator).is_displayed()

