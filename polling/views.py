# polling/views.py

from django.shortcuts import render
from django.http import Http404
from polling.models import Poll  # , Question

##Stuff I added
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from django.urls import reverse


def list_view(request):
    context = {
        "polls": Poll.objects.all(),
        "latest_question_list": Question.objects.order_by("-pub_date")[:5],
    }

    return render(request, "polling/list.html", context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {"poll": poll}
    return render(request, "polling/detail.html", context)


# ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
# ##Stuff I added after Assigment08
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polling/list.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#
#
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404
#
#     if request.method == "POST":
#         if request.POST.get("vote") == "Yes":
#             question.score += 1
#         else:
#             question.score -= 1
#         question.save()
#
#     context = {'question': question}
#     return render(request, 'polling/detail2.html', context)
#
#
#     #return HttpResponse("You're looking at question %s." % question_id)
#
# #def results(request, question_id):
#     #response = "You're looking at the results of question %s."
#     #return HttpResponse(response % question_id)
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polling/results.html', {'question': question})
#
# #def vote(request, question_id):
#     #return HttpResponse("You're voting on question %s." % question_id)
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#
#         return render(request, 'polling/detail2.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse('polling:results', args=(question.id,)))
#
