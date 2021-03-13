import os
import time
import yaml

import allure
import pytest
from selenium import webdriver
from config import config_path
# from config import config_path
from utils.log import Log
from operate.webKeywords import WebKeywords
# from utils.readYaml import datas
log = Log().logger
datas= None
with open(config_path.TEST_Element_YAML + '/' + 'loginEle.yaml',encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    f.close()
# try:
#     with open(config_path.TEST_Element_YAML + '/' + 'loginEle.yaml', encoding='utf-8') as f:
#         datas = yaml.safe_load(f)
#         f.close()
# except FileNotFoundError as file:
#     log.error("文件不存在：{0}".format(file))

@allure.feature("蜂巢投放系统后台")
class Test_photoMange:
    """
    系统
    """
    @allure.title("打开浏览器")
    def setup_class(self):

        self.web = WebKeywords()
        self.web.OpenBrowser()
    @pytest.mark.debugcase
    @allure.story("登陆")
    @pytest.mark.parametrize('listcases', datas['loginPage'])
    def test_login(self, listcases):
       # allure.dynamic.title(listcases['title'])
       testcases = listcases['cases']
       # allure.attach(testcases,"获取的关键字:")
       log.info(testcases)
       for cases in (testcases):
           listcase = list(cases.values())
           with allure.step(listcase[0]):
               print(listcase)
               func =getattr(self.web, listcase[1])
               values = listcase[2:]
               func(*values)

    @pytest.mark.debugcase
    @allure.story("素材管理_图片管理_关键字查询_按图片名称_有数据")
    @pytest.mark.parametrize('itemList',datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search01(self,itemList):
        testcases = itemList['cases']
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)

    @allure.story("素材管理_图片管理_按图片名称_关键字查询无数据")
    @pytest.mark.parametrize('itemList',datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search02(self,itemList):
        testcases = itemList['cases1']
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)

    @allure.story("素材管理_图片管理_按本地名_关键字查询有数据")
    @pytest.mark.parametrize('itemList', datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search03(self, itemList):
        testcases = itemList['cases2']
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)

    @allure.story("素材管理_图片管理_按本地名称_关键字查询无数据")
    @pytest.mark.parametrize('itemList', datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search04(self, itemList):
        testcases = itemList['cases3']
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)

    @pytest.mark.debugcase
    @allure.story("素材管理_图片管理_按订单查询_关键字查询有数据")
    @pytest.mark.parametrize('itemList', datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search05(self, itemList):
        testcases = itemList['cases4']
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)

    @pytest.mark.debugcase
    @allure.story("素材管理_图片管理_新增")
    @pytest.mark.parametrize('itemList', datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search06(self, itemList):
        testcases = itemList['cases5_add']
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)

    @allure.story("素材管理_图片管理_勾选删除_取消成功")
    @pytest.mark.parametrize('itemList', datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search07(self, itemList):
        testcases = itemList['cases6_delete']
        allure.dynamic.title(itemList['title'])
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)

    @allure.story("素材管理_图片管理_勾选删除_删除成功")
    @pytest.mark.parametrize('itemList', datas['素材管理_图片管理'])
    def test_photo_manage_kewords_search08(self, itemList):
        testcases = itemList['cases7_delete']
        allure.dynamic.title(itemList['title'])
        # allure.attach(testcases,"获取的关键字:")
        log.info(testcases)
        for cases in (testcases):
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                print(listcase)
                func = getattr(self.web, listcase[1])
                values = listcase[2:]
                func(*values)


    def teardown_class(self):
        self.web.quit()

if __name__ == '__main__':
    # pytest.main(["test_login.py::Test_photoMange::test_login::test_photo_manage_kewords_search06"])
    # pytest.main(["-s","test_login.py","-m=debugcase"])加mark.名称的方法wuwork
    pytest.main(['/maincase/test_login'])
    # pytest.main(['-v','-s','--html=report.html'])
    # os.system('allure serve ./report/index.html')