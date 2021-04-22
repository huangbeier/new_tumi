# @Author ：黄贝尔
# @Time ：2021/4/22__11:17
# #coding:utf-8
from mod.cn_mod_homepage import Homepage_mod
from selenium import webdriver
import time
import unittest
import configparser
from utils.get_conf_path import elementLocationPath
from utils.seleniumtools import new_find_element
# def login():
#     driver = webdriver.Chrome(r'C:\huang111\new_tumi\chromedriver.exe')
#     driver.get('https://www.tumi.cn/')
#     driver.maximize_window()
#     mod=Homepage_mod()
#     mod.login(driver)
#
#
# if __name__ == '__main__':
#     login()
class HOMEPAGE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conf=configparser.ConfigParser()
        cls.conf.read(elementLocationPath,encoding='utf-8')
        cls.driver=webdriver.Chrome(cls.conf.get('chrome','path'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.mod = Homepage_mod(self.driver)
        self.driver.get(self.conf.get('tumi_cn','path'))
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(2)

    # def test001_login(self):
    #     mod = Homepage_mod()
    #     mod.login(self.driver)

    def test_001_TUMIUAT_408_1(self):
        self.mod.TUMIUAT_408_1(self.driver)
        assert self.driver.current_url == self.conf.get('tumi_cn','path')

    def test_002_TUMIUAT_408_2(self):
        self.mod.TUMIUAT_408_2(self.driver)
        assert self.driver.current_url == f'{self.conf.get("tumi_cn", "path")}tumi-club/'
        assert new_find_element(self.driver,self.conf.get('homepage','vip_Privilege').split(',')).text == '会员专属礼遇'

    def test_004_TUMIUAT_408_4(self):
        self.mod.TUMIUAT_408_4(self.driver)
        assert self.driver.current_url == f'{self.conf.get("tumi_cn","path")}store-locator/'
        assert new_find_element(self.driver,self.conf.get('homepage','store_type').split(',')).text == '门店类型'

    def test_005_TUMIUAT_408_5(self):
        self.mod.TUMIUAT_408_5(self.driver)
        assert self.driver.current_url == f'{self.conf.get("tumi_cn","kefu")}'

    def test_006_TUMIUAT_408_6(self):
        self.mod.TUMIUAT_408_6(self.driver)
        assert self.driver.current_url == f'{self.conf.get("tumi_cn","path")}cart'

    def test_007_TUMIUAT_408_7(self):
        self.mod.TUMIUAT_408_7(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','login_text').split(',')).text == '登录您的TUMI.CN账号'

    def test_008_TUMIUAT_410(self):
        self.mod.TUMIUAT_410(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','keyword').split(',')).text == '建议关键字 "alp"'

    def test_009_TUMIUAT_411(self):
        self.mod.TUMIUAT_411(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','no_search').split(',')).text == '对不起，没有搜索结果'

    def test_010_TUMIUAT_412(self):
        self.mod.TUMIUAT_412(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','have_search').split(',')).text == '“ALPHA”'

    def test_010_TUMIUAT_1510_1(self):
        self.mod.TUMIUAT_1510_1(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','pro_title').split(',')).text =='各类旅行箱 - 托运旅行箱、登机箱'

    def test_011_TUMIUAT_1510_2(self):
        self.mod.TUMIUAT_1510_2(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','pro_title').split(',')).text =='各类背包 - 商务、旅行、休闲背包'

    def test_012_TUMIUAT_1510_3(self):
        self.mod.TUMIUAT_1510_3(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','pro_title').split(',')).text =='斜挎包 - 休闲斜挎包'

    def test_013_TUMIUAT_1510_4(self):
        self.mod.TUMIUAT_1510_4(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','pro_title').split(',')).text =='托特包 - 手拎包、手袋'

    def test_014_TUMIUAT_1510_5(self):
        self.mod.TUMIUAT_1510_5(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','pro_title').split(',')).text =='各类旅行配件、电子产品、钱包等'

    def test_015_TUMIUAT_1510_6(self):
        self.mod.TUMIUAT_1510_6(self.driver)
        assert new_find_element(self.driver,self.conf.get('homepage','pro_title').split(',')).text =='由可回收材料制成的环保系列'