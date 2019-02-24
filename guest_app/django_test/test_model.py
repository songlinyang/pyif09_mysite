"""用于测试Model，测试部件"""
from django.test import TestCase
from guest_app.models import Event
from datetime import datetime
class MyModelTest(TestCase):

    def setUp(self):
        Event.objects.create(name='测试发布会', status=True, limit=1000, address='北京',
                             start_time=datetime(2019, 2, 16, 15, 29))

    def tearDown(self):
        pass

    #测试用例 - 测试新增
    def test_model_create(self):
        #测试步骤 -- 创建数据   记住：Django的测试，是独立的环境，不会影响现有数据库的数据
        Event.objects.create(name='手机发布会',status=True,limit =1000,address='北京',start_time=datetime(2019,2,16,15,29))
        event = Event.objects.get(name="手机发布会")
        self.assertEqual(event.address,"北京")


    #测试用例2 - 测试查询
    def test_model_select(self):
        #测试步骤 -- 查询数据
        event = Event.objects.get(name='测试发布会')
        self.assertEqual(event.address,"北京")


    #测试用例3 - 测试修改
    def test_model_update(self):
        event = Event.objects.get(name='测试发布会')
        event.address = '上海'
        event.save()
        self.assertEqual(event.address,"上海")

    #测试用例4 - 测试删除
    def test_model_delete(self):
        event = Event.objects.filter(name='测试发布会')
        event.delete()
        self.assertEqual(len(event),0)
