from django import forms
from django.forms import ModelForm

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

