"""测试计算器 加法部件"""
import unittest
from count import Count
class MyAddTest(unittest.TestCase):

    def test_add1(self):
        #测试步骤
        count = Count()
        result = count.add(1,2)
        #实际结果
        actual_result = result
        #预期结果
        expect_result = 3

        #断言
        self.assertEqual(actual_result,expect_result)

    def test_add2(self):
        #测试步骤
        count = Count()
        result = count.add(1.1,3)
        #实际结果
        actual_result = float(result)
        #预期结果
        expect_result = 4.1

        #断言
        self.assertEqual(actual_result,expect_result)

