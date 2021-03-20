from django.db import models

# Create your models here.
from question_bank.models import BankInformation
from user.models import Orgnization, User


class Quiz(models.Model): #考试信息表
    quiz_name = models.CharField('考试名称',max_length=30)
    org_id = models.ForeignKey('考试机构id',Orgnization,on_delete=models.CASCADE)
    bank_id = models.ForeignKey('题库id',BankInformation,on_delete=models.CASCADE)
    type = models.CharField('科目类型',max_length=20)
    start_time = models.DateTimeField('开始时间')
    end_time = models.DateTimeField('结束时间')
    total_time = models.CharField('考试时间',max_length=10)
    choice_num = models.IntegerField('选择题数量')
    fill_num = models.IntegerField('填空题数量')
    total_score = models.IntegerField('总分')
    status = models.BooleanField('考试状态') #True考试进行中 False考试已结束


class Answer(models.Model): #答题记录表
    user_id = models.ForeignKey('考生id',User,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey('考试id',Quiz,on_delete=models.CASCADE)
    qtype = models.CharField('题型',max_length=10)
    question_id = models.IntegerField('题目id') #对应选择题或填空题的ｉｄ
    answer = models.CharField('考生答案',max_length=50)

