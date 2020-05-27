from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import QuestionnaireForm
from .models import QuestionYesNo

# https://www.youtube.com/watch?v=b8RpVs7bSgo&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=45

## starting arguments
global score
global question_pk
score = 0
question_pk = 1

class QuestionForm(FormView):
    template_name = 'questionnaire/question.html'

    def get(self, request):
        global question_pk
        if QuestionYesNo.objects.filter(pk=question_pk).exists():
            self.question = QuestionYesNo.objects.get(pk=question_pk)
        QuestionYesNo.objects.get(pk=question_pk)

        form = QuestionnaireForm

        return render(request,
                      self.template_name,
                      {'form': form,
                       'question': self.question},
                      )

    def post(self, request):
        global question_pk
        if QuestionYesNo.objects.filter(pk=question_pk).exists():
            self.question = QuestionYesNo.objects.get(pk=question_pk)
        else:
            question_pk = 1
            self.question = QuestionYesNo.objects.get(pk=question_pk)

        form = QuestionnaireForm(request.POST)

        if form.is_valid():
            answer = int(form.cleaned_data['answer'])
            if answer == self.question.right_answer:
                global score
                score += 1

            print(score)

            question_pk += 1

            context ={'form': form,
                      'answer': answer,
                      'question': self.question}

            return render(request,
                          self.template_name,
                          context
                          )


