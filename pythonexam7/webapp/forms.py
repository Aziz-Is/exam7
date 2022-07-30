from django.forms import ModelForm
from .models import Poll, Choice


class MyForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class MyChoiceForm(ModelForm):
    class Meta:
        model = Choice
        exclude=[]