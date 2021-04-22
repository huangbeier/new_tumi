# @Author ：黄贝尔
# @Time ：2021/4/22__11:11
# #coding:utf-8
from obj.cn_obj_homepage import Homepage_pro
class Homepage_mod():

    def login(self,driver):
        pro=Homepage_pro(driver)
        pro.click_login_register_btn()
        pro.input_phone()
        pro.input_password()
        pro.click_login_btn()
        pro.click_close_login()

