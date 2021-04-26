# @Author ：黄贝尔
# @Time ：2021/4/22__11:46
# #coding:utf-8
import os
import time
# print(os.path.dirname(__file__))
parentDirPath = os.path.dirname(os.path.dirname(__file__))

elementLocationPath = os.path.join(parentDirPath, u'config\config.ini')

Chromepath=os.path.join(parentDirPath, u'chromedriver.exe')

test_url=r'https://www.tumi.cn/'
#NBBKZIBDBVDTURJG    TG笔记本
auth_code = 'LXHRNCHDCWUYAQGG'#邮箱授权码
excelpath=os.path.join(parentDirPath, u'data\\t_01.xlsx')
reportpath=os.path.join(parentDirPath, u'report\\{}Test_report.html'.format(time.strftime('%Y-%m-%d')))
logpath=os.path.join(parentDirPath, u'config\\log')


if __name__ == '__main__':
    print(Chromepath)
    print(elementLocationPath)
    print(parentDirPath)
    print(excelpath)
    print(reportpath)
    print(logpath)