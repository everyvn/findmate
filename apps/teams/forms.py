from django import forms
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget

CHOICES = [
    ('1', '창업'),
    ('2', '취미'),
    ('3', '사이드프로젝트'),
    ('4', '스터디'),
    ('5', 'ETC'),
]

class TeamRegisterForm(forms.ModelForm):
    name = forms.CharField(label='팀 이름', widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '팀 이름을 알려주세요 (최대 20자)'
    }))
    short_description = forms.CharField(label='팀 소개', widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '간략한 팀 소개를 작성해주세요 (최대 50자)'
    }))
    purpose = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={
        'required':'required'
    }))
    logo = forms.FileField(label='팀 로고', widget=forms.FileInput(attrs={
        'class':'hidden',
        'required':'required'
    }))
    class Meta:
        model = Team
        field = '__all__'
        exclude = ()