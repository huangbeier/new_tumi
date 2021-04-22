# @Author ：黄贝尔
# @Time ：2021/4/22__11:17
# #coding:utf-8
from mod.cn_mod_homepage import Homepage_mod
from selenium import webdriver
import time
import unittest
import configparser
from utils.get_conf_path import elementLocationPath
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
        self.driver.get(self.conf.get('tumi_cn','path'))
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(2)

    def test001_login(self):
        mod = Homepage_mod()
        mod.login(self.driver)

