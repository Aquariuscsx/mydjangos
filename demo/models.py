from django.db import models


# Create your models here.
class User(models.Model):
    #
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    # 创建字符串属性
    password = models.CharField(max_length=32)
    sex = models.IntegerField(max_length=1)
    phone = models.CharField(max_length=11)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # auto_now=True  创建的时候会添加 更新的时候也会添加
    create_date = models.DateField( auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)#这两个不要重复出现
    head_ing = models.ImageField(upload_to='uploads/')
