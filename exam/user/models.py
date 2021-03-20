from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField('用户名',max_length=11)
    nickname = models.CharField('nickname',max_length=30,default=username)
    password = models.CharField('密码',max_length=30)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    updated_time = models.DateTimeField('修改时间',auto_now=True)
    phone = models.CharField('手机号',max_length=11)

class Orgnization(models.Model):
    org_name = models.CharField('机构名称',max_length=30)
    type = models.CharField('类型',max_length=20)
    phone = models.CharField('手机号',max_length=11)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)

