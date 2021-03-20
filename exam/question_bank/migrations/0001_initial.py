# Generated by Django 2.2.12 on 2021-03-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.IntegerField(verbose_name='出题机构id')),
                ('bank_name', models.CharField(max_length=30, verbose_name='题库名')),
                ('bank_type', models.CharField(max_length=15, verbose_name='题库类型')),
                ('choice_num', models.IntegerField(verbose_name='选择题数量')),
                ('fill_num', models.IntegerField(verbose_name='填空题数量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='题目内容')),
                ('answer', models.CharField(max_length=6, verbose_name='答案')),
                ('choice_A', models.CharField(max_length=50, verbose_name='选项A')),
                ('choice_B', models.CharField(max_length=50, verbose_name='选项B')),
                ('choice_C', models.CharField(max_length=50, verbose_name='选项C')),
                ('choice_D', models.CharField(max_length=50, verbose_name='选项D')),
                ('bank_id', models.IntegerField(verbose_name='题库id')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionFill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='题目内容')),
                ('answer', models.CharField(max_length=100, verbose_name='答案')),
                ('bank_id', models.IntegerField(verbose_name='题库id')),
            ],
        ),
    ]