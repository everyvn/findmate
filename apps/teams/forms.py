from django import forms
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget

class TeamRegisterForm(forms.ModelForm):
    class Meta:
        model = Team
        field = '__all__'
        exclude = ()