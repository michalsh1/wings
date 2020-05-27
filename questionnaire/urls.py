
from django.urls import path
from questionnaire.views import QuestionForm


urlpatterns = [
    path('', QuestionForm.as_view(), name='question_form'),
]

