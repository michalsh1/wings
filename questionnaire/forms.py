from django import forms
from django.forms.widgets import RadioSelect, Textarea
from .models import QuestionYesNo, RightAnswer


class YesNoAnswers(object):
    YES = 1
    NO = 0

    choices = (
        (YES, 'Yes'),
        (NO, 'No'),
        )


class QuestionnaireForm(forms.Form):
    # answer = forms.CharField(max_length=20)
    answer = forms.ChoiceField(choices=YesNoAnswers.choices, label=("Yes_No"), widget=RadioSelect)
