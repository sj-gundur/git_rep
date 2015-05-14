from django import forms
from django.forms import ModelForm
from readreview.models import comments

class commentsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    comments = forms.CharField(label='Comments', max_length=100)

