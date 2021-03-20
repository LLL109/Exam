import json

from django.core.cache import cache
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from question_bank.models import QuestionChoice, QuestionFill
from user.models import Orgnization, User
from .models import Quiz,Answer


class QuizView(View):
    def get(self, request: HttpRequest):
        quiz_id = request.GET.get('quiz_id')
        page_index = request.GET.get('page_index')
        # try:
        #     quiz = Quiz.objects.get(quiz_id=quiz_id)
        # except:
        #     return JsonResponse({'code': 10200, 'error': '考试id错误'})
        # quiz_name = quiz.quiz_name
        quiz_name = '中华古诗词大赛'
        # start_time = quiz.start_time
        # end_time = quiz.end_time
        # total_time = quiz.total_time
        total_time = 100
        # choice_num = quiz.choice_num
        choice_num = 1
        # fill_num = quiz.fill_num
        fill_num  = 1
        # cache_key = f"quiz_{quiz_id}:question_id"
        # q_li = cache.get(cache_key)
        # if not q_li:
        #     return JsonResponse({'code': 10200, 'error': '考试已结束！'})
        # try:
        #     question_id = q_li[page_index]
        # except:
        #     return JsonResponse({'code': 10200, 'error': 'page_index有误！'})
        if int(page_index) + 1 <= choice_num:
            # choice = QuestionChoice.objects.get(id=question_id)
            data = {
                'quiz_name': quiz_name,
                'total_time': total_time,
                'question': 'choice.question',
                'choice_A': 'choice.choice_A',
                'choice_B': 'choice.choice_B',
                'choice_C': 'choice.choice_C',
                'choice_D': 'choice.choice_D',
                'type': 'choice',
                'ques_num':choice_num+fill_num, #题目总数
            }
            res = {'code': 200, 'data': data}
        else:
            # fill = QuestionFill.objects.get(id=question_id)
            res = {'code':200,'data':{
                'quiz_name':quiz_name,
                'question':'静夜思的作者是_____',
                'type': 'fill',
                'ques_num': choice_num + fill_num,
            }}

        return JsonResponse(res)


    def post(self,request:HttpRequest):
        # 记录考生答题记录
        # {'u_id': 10, 'quiz_id': '1', 'page_index': 0, 'answer': 'A'}
        py_obj = json.loads(request.body)
        print(py_obj)
        u_id = py_obj['u_id']
        quiz_id = py_obj['quiz_id']
        page_index = py_obj['page_index']
        qtype = py_obj['qtype']
        cache_key = f"quiz_{quiz_id}:question_id"
        cache.set(cache_key,[1,2,3,4,5,6,7],1800)
        question_id = cache.get(cache_key)[page_index]
        print(question_id)
        # Answer.objects.create(user_id=u_id,quiz_id=quiz_id,qtype=qtype,question_id=question_id)
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

