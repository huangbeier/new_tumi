# -*- coding: utf-8 -*-
#   __author__:黄贝尔
#   2021-04-25
import unittest

from utils.get_conf_path import reportpath
from utils.ClassicHTMLTestRunner import HTMLTestRunner

#自动收集测试用例


testcase = unittest.defaultTestLoader.discover('../work/case', 'test_*.py')

#自动运行case并生成报告 htmltestrunner
filePath = reportpath
title = '测试报告'
tester = 'beier'

with open(filePath,'wb') as f:
    runner =HTMLTestRunner(stream=f,title=title,tester=tester)
    runner.run(testcase)
    
#运行完之后，发送邮件
# mail = SendMail('smtp.163.com')
# send_address = "beier0917@163.com"
# send_password = auth_code
# receive_address = ['953564459@qq.com', '2482821110@qq.com']
# title = "测试报告"
# content = "测试报告在附件中"
# attachfilepath = reportpath
# mail.send_mail(send_address, send_password, receive_address, title, content, file=attachfilepath)
