"""用于测试视图，测试部件"""
import unittest
from django.test import TestCase
from django.contrib.auth.models import User

class MyViewTest(TestCase):

    def setUp(self):
        #User.objects.create_user("admin","admin@qq.com","admin123456")
        pass
    def tearDown(self):
        pass

    #测试用例1 - 测试是否能进入登录页，状态是否为200
    def test_login_status_code(self):
        rsp = self.client.get("index/")
        self.assertEqual(rsp.status_code,200)

    #测试用例2 - 测试是否返回的是登录页
    def test_login_page(self):
        rsp = self.client.get("index/")
        self.assertTemplateUsed(rsp,"index.html")

    #测试用例2 - 测试用户名为空，密码为空，登录失败
    def test_login_fail_because_username_password_is_null(self):
        test_data = {
            "username": "",
            "password":""
        }
        rsp = self.client.post("/login_action/",data=test_data)
        self.assertIn(rsp.content,"用户名或者密码不能为空~")


    #测试用例3 - 测试用户名错误，密码错误，登录失败
    def test_login_fail_because_username_password_is_fault(self):
        test_data = {
            "username": "error",
            "password": "error"
        }
        rsp = self.client.post("/login_action/",data=test_data)
        self.assertIn(rsp.content,"用户名或者密码错误~")

    #测试用例4 - 测试用户名正确，密码正确，登录成功
    def test_login_success(self):
        test_data = {
            "username": "admin",
            "password": "admin123456"
        }
        rsp = self.client.post("/login_action/",data=test_data)
        self.assertEqual(rsp.status_code,302)