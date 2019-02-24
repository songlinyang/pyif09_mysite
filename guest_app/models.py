from django.db import models

# Create your models here.
"""
活动：
参与人员：
"""

class Event(models.Model):
    name = models.CharField("名称",max_length=50) #名称
    status = models.BooleanField("状态",default=True)
    limit = models.IntegerField("人数")
    address = models.CharField("地址",max_length=100)
    start_time = models.DateTimeField("时间")
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Guest(models.Model):
    """嘉宾表"""
    event = models.ForeignKey(Event,on_delete=models.Case) #与活动进行关联 什么是外键
    real_name = models.CharField("姓名",max_length=64) #姓名
    phone = models.CharField("手机号",max_length=16) #手机号
    email = models.EmailField("邮箱") #邮箱
    sign = models.BooleanField("签到")  #签到
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.real_name




"""
新增
e1 = Event.objects.create(name="荣耀手机",address="深圳"",limit=2000,start
_time="2018-12-23 09:25:12")

更新
e2 = Event.objects.get(id=6)
e2.name = "荣耀play手机"
e2.save()

e = Event.objects.get(id=3)

批量更新
Event.objects.get(id=6).

"""