

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from polls.models import Question


def save(request, question_id):
    q = request.POST['q']
    question = Question.objects.get(id=question_id)
    question.question_text = q
    question.save()

    return HttpResponse('수정 완료')


def edit(request, question_id):
    q= Question.objects.get(id=question_id)

    return render(
        request, 'polls/edit.html', {'q':q}
    )


def vote(request, question_id):
    q = Question.objects.get(id=question_id)

    try:
        select = request.POST['select']

        c = q.choice_set.get(id=select)

        c.votes += 1
        c.save()

        print(select)
    except:
        pass

    return render(
        request,
        'polls/result.html',
        {'q':q}
    )




def detail(request, question_id):
    q = Question.objects.get(id=question_id) #조건에 맞는 data 1개 조회
    c = q.choice_set.all()
    #choice=''
    #for a in c:
    #    choice += a.choice_text
    #                     템플릿, 컨텍스트(=데이터=모델)
    return render(request,
                  'polls/detail.html',
                  {
                      'question': q.question_text,
                      'num': q.id,
                      'choice': c
                  })
    #return HttpResponse(q.question_text + '<br>'+ choice) #문자열 + 리스트 x


def detail2(request, num1, num2):
    return HttpResponse(num1 + num2)


def add(request):
    q = request.GET('q')

    Question.objects.create(question_text=q, pub_date=timezone.now())
    return HttpResponse('')


def index(request):

    questions = Question.objects.all()
    #             request, 템플릿               컨텍스트(모델/데이터 {}형태로.
    return render(request, 'polls/index.html', {'question':questions})
    #index.html로 넘어가면 questions는 잊어도 되 다 넘어간 뒤거든.


    #1번 create를 이용하여 데이터 입력
    #Question.objects.create()

    #2번 save를 이용하여 데이터 입력
    #Question(question_text='aaaa', pub_date=timezone.now()).save()


    # q=Question.objects.all()[0]
    # choices = q.choice_set.all()
    #
    # print(q.question_text)
    # print(choices[0].choice_text)
    # print(choices[1].choice_text)
    # print(choices[2].choice_text)

    return HttpResponse('polls index')
