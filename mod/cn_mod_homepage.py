# @Author ：黄贝尔
# @Time ：2021/4/22__11:11
# #coding:utf-8
from obj.cn_obj_homepage import Homepage_obj


class Homepage_mod():
    def __init__(self,driver):
        self.obj=Homepage_obj(driver)

    def login(self,driver):
        obj=Homepage_obj(driver)
        obj.click_login_register_btn()
        obj.input_phone()
        obj.input_password()
        obj.click_login_btn()
        obj.click_close_login()

    def login2(self,driver):
        obj = Homepage_obj(driver)
        obj.click_login_register_btn()
        obj.input_phone()
        obj.input_password2()
        obj.click_login_btn()
        obj.click_close_login()

    def TUMIUAT_408_1(self,driver):
        obj = Homepage_obj(driver)
        obj.click_logo()

    def TUMIUAT_408_2(self,driver):
        obj = Homepage_obj(driver)
        obj.click_vip_club()
        driver.switch_to_window(driver.window_handles[-1])

    def TUMIUAT_408_4(self,driver):
        obj = Homepage_obj(driver)
        obj.click_offline_store()
        driver.switch_to_window(driver.window_handles[-1])

    def TUMIUAT_408_5(self,driver):
        obj = Homepage_obj(driver)
        obj.click_customer_service()
        driver.switch_to_window(driver.window_handles[-1])

    def TUMIUAT_408_6(self,driver):
        obj = Homepage_obj(driver)
        obj.click_cart()
        driver.switch_to_window(driver.window_handles[-1])

    def TUMIUAT_408_7(self,driver):
        obj = Homepage_obj(driver)
        obj.click_login_register_btn()

    def TUMIUAT_410(self,driver):
        obj = Homepage_obj(driver)
        obj.input_search('alp')

    def TUMIUAT_411(self,driver):
        obj = Homepage_obj(driver)
        obj.input_search('alpp')
        obj.click_search_btn()
        driver.switch_to_window(driver.window_handles[-1])

    def TUMIUAT_412(self,driver):
        obj = Homepage_obj(driver)
        obj.input_search('alp')
        obj.click_suggested_keyword()

    def TUMIUAT_1510_1(self,driver):
        obj = Homepage_obj(driver)
        obj.click_f_luggage()
        driver.switch_to_window(driver.window_handles[-1])
    
    def TUMIUAT_1510_2(self,driver):
        obj = Homepage_obj(driver)
        obj.click_f_backpacks()
        driver.switch_to_window(driver.window_handles[-1])
    
    def TUMIUAT_1510_3(self,driver):
        obj = Homepage_obj(driver)
        obj.click_f_totes()
        driver.switch_to_window(driver.window_handles[-1])

    def TUMIUAT_1510_4(self,driver):
        obj = Homepage_obj(driver)
        obj.click_f_crossbodies()
        driver.switch_to_window(driver.window_handles[-1])
    
    def TUMIUAT_1510_5(self,driver):
        obj = Homepage_obj(driver)
        obj.click_f_accessories()
        driver.switch_to_window(driver.window_handles[-1])

    def TUMIUAT_1510_6(self,driver):
        obj = Homepage_obj(driver)
        obj.click_f_recycled()
        driver.switch_to_window(driver.window_handles[-1])
        




