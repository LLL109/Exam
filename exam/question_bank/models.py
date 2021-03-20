from django.db import models


# Create your models here.
class QuestionChoice(models.Model):
    question = models.CharField('题目内容', max_length=100)
    answer = models.CharField('答案', max_length=6)
    choice_A = models.CharField('选项A', max_length=50)
    choice_B = models.CharField('选项B', max_length=50)
    choice_C = models.CharField('选项C', max_length=50)
    choice_D = models.CharField('选项D', max_length=50)
    bank_id = models.IntegerField('题库id')


class QuestionFill(models.Model):
    question = models.CharField('题目内容', max_length=100)
    answer = models.CharField('答案', max_length=100)
    bank_id = models.IntegerField('题库id')


class BankInformation(models.Model):
    org_id = models.IntegerField('出题机构id')
    bank_name = models.CharField('题库名', max_length=30)
    bank_type = models.CharField('题库类型', max_length=15)
    choice_num = models.IntegerField('选择题数量')
    fill_num = models.IntegerField('填空题数量')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
