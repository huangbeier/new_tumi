# @Author ：黄贝尔
# @Time ：2021/4/22__11:17
# #coding:utf-8
from mod.cn_mod_homepage import Homepage_mod
from selenium import webdriver
import time

def login():
    driver = webdriver.Chrome(r'C:\huang111\new_tumi\chromedriver.exe')
    driver.get('https://www.tumi.cn/')
    driver.maximize_window()
    mod=Homepage_mod()
    mod.login(driver)


if __name__ == '__main__':
    login()

