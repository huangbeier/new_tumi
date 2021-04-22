# @Author ：黄贝尔
# @Time ：2021/4/22__10:46
# #coding:utf-8
import configparser
from utils.seleniumtools import new_find_element
from selenium import webdriver
import time
class Homepage_pro:
    def __init__(self,driver):
        self.driver = driver
        self.conf=configparser.ConfigParser()
        self.conf.read(r'C:\huang111\new_tumi\utils\config.ini',encoding='utf-8')


    def click_login_register_btn(self):
        new_find_element(self.driver,self.conf.get('homepage','login_register_btn').split(',')).click()
        time.sleep(1)

    def input_phone(self):
        new_find_element(self.driver,self.conf.get('homepage','phone').split(',')).send_keys(self.conf.get('info','username1'))

    def input_password(self):
        new_find_element(self.driver, self.conf.get('homepage', 'password').split(',')).send_keys(self.conf.get('info', 'password1'))

    def click_login_btn(self):
        new_find_element(self.driver,self.conf.get('homepage','login_btn').split(',')).click()
        time.sleep(1.5)

    def click_close_login(self):
        new_find_element(self.driver,self.conf.get('homepage','close_login').split(',')).click()
        time.sleep(1)

