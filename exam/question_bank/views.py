from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import csv
# Create your views here.
from django.views import View


class ChoiceView(View):
    def get(self, request):
        if 'type' not in request.GET.keys():
            return render(request, 'index.html')
        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="question_bank.csv"'
            writer = csv.writer(response)
            writer.writerow(
                ['题目内容', '答案', '选项A', '选项B', '选项C', '选项D'])
            # writer.writerow('\n')
            writer.writerow(
                ['题目内容', '答案', '题库名称'])
            return response

    def post(self, request):
        bank_name = request.POST['bank_name']
        bank_type = request.POST['bank_type']
        a_file = request.FILES['question_bank']
        data = a_file.file.read().decode()
        print(bank_name,bank_type)
        print(data)

        # Content.objects.create(desc=title, myfile=a_file)
        return JsonResponse({'code': 200})
