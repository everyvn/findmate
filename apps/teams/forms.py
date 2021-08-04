from django import forms
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget

class TeamRegisterForm(forms.ModelForm):
    name = forms.CharField(label='팀 이름', widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '팀 이름을 알려주세요 (최대 20자)'
    }))
    short_description = forms.CharField(label='팀 소개', widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '간략한 팀 소개를 작성해주세요 (최대 50자)'
    }))
    logo = forms.FileField(label='팀 로고', widget=forms.FileInput(attrs={
        'class':'hidden',
    }))
    class Meta:
        model = Team
        field = '__all__'
        exclude = ()