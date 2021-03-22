import json
import time

from django.core.cache import cache
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from question_bank.models import QuestionChoice, QuestionFill
from user.models import Orgnization, User
from .models import Quiz, Answer, Score


class QuizView(View):
    def get(self, request: HttpRequest):
        quiz_id = request.GET.get('quiz_id')
        page_index = request.GET.get('page_index')
        try:
            quiz = Quiz.objects.get(quiz_id=quiz_id)
        except:
            return JsonResponse({'code': 10200, 'error': '考试id错误'})
        quiz_name = quiz.quiz_name
        quiz_name = '中华古诗词大赛'
        start_time = quiz.start_time
        end_time = quiz.end_time
        total_time = quiz.total_time
        total_time = 100
        choice_num = quiz.choice_num
        fill_num = quiz.fill_num
        cache_key = f"quiz_{quiz_id}:question_id"
        q_li = cache.get(cache_key)
        if not q_li:
            return JsonResponse({'code': 10200, 'error': '考试已结束！'})
        try:
            question_id = q_li[page_index]
        except:
            return JsonResponse({'code': 10200, 'error': 'page_index有误！'})
        if int(page_index) + 1 <= choice_num:
            choice = QuestionChoice.objects.get(id=question_id)
            data = {
                'quiz_name': quiz_name,
                'total_time': total_time,
                'question': choice.question,
                'choice_A': choice.choice_A,
                'choice_B': choice.choice_B,
                'choice_C': choice.choice_C,
                'choice_D': choice.choice_,
                'type': 'choice',
                'ques_num':choice_num+fill_num, #题目总数
            }
            res = {'code': 200, 'data': data}
        else:
            fill = QuestionFill.objects.get(id=question_id)
            res = {'code':200,'data':{
                'quiz_name':quiz_name,
                'question':fill.question,
                'type': 'fill',
                'ques_num': choice_num + fill_num,
            }}

        return JsonResponse(res)


    def post(self,request:HttpRequest):
        # 记录考生答题记录
        # {'u_id': 10, 'quiz_id': '1', 'page_index': 0, 'answer': 'A'}
        py_obj = json.loads(request.body)
        # print(py_obj)
        u_id = py_obj['u_id']
        quiz_id = py_obj['quiz_id']
        page_index = py_obj['page_index']
        qtype = py_obj['qtype']
        cache_key = f"quiz_{quiz_id}:question_id"
        # cache.set(cache_key,[1,2,3,4,5,6,7],1800) 
        question_id = cache.get(cache_key)[page_index]
        print(question_id)
        Answer.objects.create(user_id=u_id,quiz_id=quiz_id,qtype=qtype,question_id=question_id)
        return JsonResponse({'code':200})


def quiz_info(request:HttpRequest): # 考试信息页
    u_id = request.GET.get('u_id')
    quiz_id = request.GET.get('quiz_id')
    try:
        user = User.objects.get(id=u_id)
    except:
        return JsonResponse({'code':10200,'error':'用户不存在'})
    try:
        quiz = Quiz.objects.get(id=quiz_id)
    except:
        return JsonResponse({'code':10201,'error':'考试id有误'})
    org = Orgnization.objects.get(id=quiz.org_id)
    data = {
        'quiz_name':quiz.quiz_name,
        'username':user.username,
        'org_name':org.name,
        'total_score':quiz.total_score,
        'total_num':quiz.choice_num+quiz.fill_num,
        'start_time':quiz.start_time,
        'end_time': quiz.end_time,
    }
    return JsonResponse({'code': 200, 'data': data})


def cal_score(answer_list,total_num,total_score):
    correct = 0
    mistake = 0
    for answer in answer_list:
        if answer.qtype == 'choice':
            question = QuestionChoice.objects.get(id=answer.question_id)
        else:
            question = QuestionFill.objects.get(id=answer.question_id)
        if question.answer == answer.answer:
            correct +=1
        else:
            mistake +=1
    single_score = total_score / total_num
    score = total_score - single_score * mistake
    return correct,mistake,score


def get_rank(score_list,user):
    rank = 1
    for score in score_list:
        if score.user == user:
            return rank
        rank +=1


def get_score(request:HttpRequest):
    u_id = request.GET.get('u_id')
    quiz_id = request.GET.get('quiz_id')
    try:
        user = User.objects.get(id=u_id)
    except:
        return JsonResponse({'code': 10200, 'error': '用户不存在'})
    try:
        quiz = Quiz.objects.get(id=quiz_id)
    except:
        return JsonResponse({'code':10201,'error':'考试id有误'})
    username = user.username
    quiz_time = time.time()-time.mktime(time.strptime(quiz.start_time, "%Y/%m/%d %H:%M:%S")) #考试时间
    answer_list = Answer.objects.filter(user=user,quiz=quiz)
    total_num = quiz.choice_num+quiz.fill_num
    total_score = quiz.total_score
    correct,mistake,score = cal_score(answer_list,total_num,total_score)
    Score.objects.create(user=user,quiz=quiz,score=score)
    score_list = Score.objects.filter(quiz=quiz).order_by('-score')
    rank = get_rank(score_list,user)
    res = {'code':200,'data':{'username':username,'score':score,'quiz_time':quiz_time,'correct':correct,'mistake':mistake,'rank':rank}}
    return JsonResponse(res)