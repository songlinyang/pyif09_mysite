"""用于运行测试"""
import unittest
from HTMLTestRunner import HTMLTestRunner
suit = unittest.defaultTestLoader.discover("./","*.py")
report = open("./report.html",'wb')
runner = HTMLTestRunner(stream=report,title='测试报告',description='这是测试计算器的一个结果报告')
runner.run(suit)
report.close()