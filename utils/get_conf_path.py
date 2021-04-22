# @Author ：黄贝尔
# @Time ：2021/4/22__11:46
# #coding:utf-8
import os

# print(os.path.dirname(__file__))
parentDirPath = os.path.dirname(os.path.dirname(__file__))
#print(parentDirPath)
elementLocationPath = os.path.join(parentDirPath, u'utils\config.ini')
#print(elementLocationPath)