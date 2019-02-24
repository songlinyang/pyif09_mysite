"""测试计算器 减法部件"""
import unittest
from count import Count
class MySubTest(unittest.TestCase):

    def test_sub1(self):
        #测试步骤
        count = Count()
        result = count.sub(3,1)
        #实际结果
        actual_result = result
        #预期结果
        expect_result = 2
        #断言
        self.assertEqual(actual_result,expect_result)

    def test_sub2(self):
        #测试步骤
        count = Count()
        result = count.sub(3.1,2.1)
        #实际结果
        actual_reuslt = result
        #预期结果
        expect_result = 1
        #断言
        self.assertEqual(actual_reuslt,expect_result)