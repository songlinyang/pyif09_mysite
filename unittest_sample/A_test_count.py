"""方法1：使用main方式执行单个测试类的全部用例"""
__author__ = 'slyang'

import unittest
from count import Count

#创建一个测试类，但是必须要继承unit
class MyTest(unittest.TestCase):



    # 用例1-- 测试整数加法
    def test_b_add1(self):
        #测试步骤
        count = Count()
        result = count.add(1,2)
        #实际结果
        actual_result = result
        #预期结果
        expect_result = 3
        #断言
        self.assertEqual(expect_result,actual_result)
    # 用例2-- 测试小数加法
    def test_a_add2(self):
        #测试步骤
        count = Count()
        result = count.add(1.1,2.13)
        #实际结果
        actual_result = float(result)
        #预期结果
        expect_reuslt = 3.23
        #断言
        self.assertEqual(expect_reuslt,actual_result)

    #用例3-- 测试整数减法
    def test_B_sub1(self):
        pass

    #用例4-- 测试小数减法
    def test_A_sub2(self):
        pass

if __name__ == '__main__':
    #方法1 --无顺序
    #unittest.main()
    #方法2 --无顺序
    suit = unittest.TestSuite()
    suit.addTest(MyTest("test_add1"))
    suit.addTest(MyTest("test_add2"))

    runner = unittest.TextTestRunner()
    runner.run(suit)
    #方法3 --每一个文件，对应一个需要测试的测试部件，一个测试部件存在同一个部件的多个测试用例

