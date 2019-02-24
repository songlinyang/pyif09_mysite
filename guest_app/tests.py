# # -*- coding:utf-8 -*-
#
# from django.test import TestCase
# from guest_app.models import Guest,Event
# from datetime import datetime
# from django.contrib.auth.models import User
# # Create your tests here.
# class TestModels(TestCase):
#
#     def setUp(self):
#         Event.objects.create(name="测试发布会", status=True, limit=1000, address="北京",
#                             start_time=datetime(2019, 8, 10, 14, 0, 0))
#     def test_event_select(self):
#         event = Event.objects.get(name="测试发布会")
#         print("发布会地址",event.address)
#         self.assertEqual(event.address,"北京")
#
#     def test_event_delete(self):
#         event = Event.objects.get(name="测试发布会")
#         event.delete()
#         event = Event.objects.filter(name="测试发布会")
#         print("发布会个数:",len(event))
#         self.assertEqual(len(event),0)
#
#     def test_event_update(self):
#         event = Event.objects.get(name="测试发布会")
#         event.address = "上海"
#         event.save()
#         event = Event.objects.get(name="测试发布会")
#         self.assertEqual(event.address,"上海")
#
#     def test_event_create(self):
#
#         event = Event.objects.get(name="测试发布会")
#         print(event.address)
#         print(event.start_time)
#         self.assertEqual(event.address,"北京")
#         self.assertEqual(event.start_time,datetime(2019,8,10,14,0,0))
#
# class TestViews(TestCase):
#
#     def setUp(self):
#         User.objects.create_user("user")
#
#     def tearDown(self):
#         pass
#
#     def test_index_page_renders_index_template(self):
#         """断音是否用了给定的index.html模板响应"""
#         response = self.client.get("/")
#         self.assertEqual(response.status_code,200)
#
#
#     def test_username_passwor_null(self):
#         test_data = {"username":"","password":""}
#         response = self.client.post("/login_action/",data=test_data)
#         self.assertEqual(response.status_code,200)
#         resp_html = response.content.decode(encoding="utf-8")
#         self.assertIn("用户名或密码错误",resp_html)
#         print(response.content)
#
#     def test_success(self):
#         test_data = {"username":"admin","password":"admin123456"}
