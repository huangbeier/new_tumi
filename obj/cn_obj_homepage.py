# @Author ：黄贝尔
# @Time ：2021/4/22__10:46
# #coding:utf-8
import configparser
from utils.seleniumtools import new_find_element
from utils.get_conf_path import elementLocationPath
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
class Homepage_obj:
    def __init__(self,driver):
        self.driver = driver
        self.conf=configparser.ConfigParser()
        self.conf.read(elementLocationPath,encoding='utf-8')


    def click_login_register_btn(self):
        new_find_element(self.driver,self.conf.get('homepage','login_register_btn').split(',')).click()
        time.sleep(1)

    def input_phone(self):
        new_find_element(self.driver,self.conf.get('homepage','phone').split(',')).send_keys(self.conf.get('info','username1'))

    def input_password(self):
        new_find_element(self.driver, self.conf.get('homepage', 'password').split(',')).send_keys(self.conf.get('info', 'password1'))

    def input_password2(self):
        new_find_element(self.driver, self.conf.get('homepage', 'password').split(',')).send_keys(self.conf.get('info', 'password2'))

    def click_login_btn(self):
        new_find_element(self.driver,self.conf.get('homepage','login_btn').split(',')).click()
        time.sleep(1.5)

    def click_close_login(self):
        new_find_element(self.driver,self.conf.get('homepage','close_login').split(',')).click()
        time.sleep(1)

    def click_logo(self):
        new_find_element(self.driver,self.conf.get('homepage','logo').split(',')).click()

    def click_vip_club(self):
        new_find_element(self.driver,self.conf.get('homepage','vip_club').split(',')).click()

    def click_offline_store(self):
        new_find_element(self.driver, self.conf.get('homepage', 'offline_store').split(',')).click()

    def click_customer_service(self):
        new_find_element(self.driver, self.conf.get('homepage', 'customer_service').split(',')).click()

    def click_cart(self):
        new_find_element(self.driver, self.conf.get('homepage', 'cart').split(',')).click()

    def input_search(self,txt):
        new_find_element(self.driver, self.conf.get('homepage', 'search').split(',')).send_keys(txt)
        time.sleep(5)
        #ActionChains(self.driver).move_to_element(new_find_element(self.driver, self.conf.get('homepage', 'search').split(','))).perform()

    def click_suggested_keyword(self):
        new_find_element(self.driver, self.conf.get('homepage', 'suggested_keyword').split(',')).click()

    def click_search_btn(self):
        new_find_element(self.driver, self.conf.get('homepage', 'search_btn').split(',')).click()

    def click_f_luggage(self):
        new_find_element(self.driver, self.conf.get('homepage', 'f_luggage').split(',')).click()

    def click_f_backpacks(self):
        new_find_element(self.driver, self.conf.get('homepage', 'f_backpacks').split(',')).click()

if __name__ == '__main__':
    #driver=webdriver.Chrome(r'C:\huang111\new_tumi\chromedriver.exe')
    #driver.get(r'https://www.tumi.cn/')
    conf = configparser.ConfigParser()
    conf.read(elementLocationPath, encoding='utf-8')
    #a=f'{conf.get("tumi_cn", "path")}'+'tumi-club/'
    b=conf.get('homepage', 'vip_Privilege').split(',')
    #c=new_find_element(driver, conf.get('homepage', 'vip_Privilege').split(',')).text
    print(b)
    print(type(c))
