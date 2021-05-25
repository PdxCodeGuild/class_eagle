from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

def index(request):
    # print('-'*10)
    # question = Question.objects.get(id=1)
    # question = Question.objects.get(question_text='What is your favorite color?')
    # print(question.question_text)
    # print('-'*10)
    # questions = Question.objects.all()
    # for question in questions:
    #     print(question.question_text)
    #     print(question.pub_date)
    #     print()
    # print('-'*10)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)

    # print('-'*20)

    # choice = Choice.objects.get(choice_text='Apples')
    # print(choice.id) # 1
    # print(choice.choice_text) # Apples
    # print(choice.question_id) # 2
    # print(choice.question.question_text) # What is your favorite fruit?

    # print('-'*20)

    # question = Question.objects.get(question_text='What is your favorite fruit?')
    # print(question.id) # 2
    # print(question.question_text) # What is your favorite fruit?
    # print(question.choice_set.all()) # <QuerySet [<Choice: Apples>, <Choice: Bananas>, <Choice: Kiwi>]>
    # for choice in question.choice_set.all():
    #     print(choice.choice_text)
    

    # print('-'*20)






    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    print(request.POST)
    question = get_object_or_404(Question, pk=question_id)
    try:
        # choice_id = request.POST['choice']
        # choice = Choice.objects.get(id=choice_id)
        # choice = Choice.objects.get(id=choice_id, question_id=question_id)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

