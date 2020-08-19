import requests
import unittest
import common.HTMLTestRunnerNew as HT
import time
#设置一个装用例的容器
suite = unittest.TestSuite()
#设置一个发现用例的工具
load = unittest.defaultTestLoader
#用load发现用例
testcases = load.discover('test_cases',pattern='test*.py',top_level_dir=None)
#把发现的用例放进容器里
suite.addTest(testcases)
#设置测试报告文档的名字---设计成固定的名字reporter+当前系统时间+html
#currenttime = time.strftime("%Y-%m-%d %H-%M-%S")
filename = r'report/reporter.html'
#生成测试报告 1、保证包要在common 2、引入import common.HTMLTestRunnerNew
with open(filename,'wb+')as fp:
    runner = HT.HTMLTestRunner(stream=fp,title='学院管理系统接口测试报告',description='aaabbb',tester='cp')
    runner.run(suite)


