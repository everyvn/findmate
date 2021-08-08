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
    team_banner = forms.FileField(label='팀 배너', widget=forms.FileInput(attrs={
        'class':'hidden',
        'required':'required'
    }))
    class Meta:
        model = Team
        field = '__all__'
        exclude = ()


CAREERS = [
    ('1','경력 무관'),
    ('2','2년 미만'),
    ('3','5년 미만'),
    ('4','10년 미만'),
    ('5','10년 이상'),
]


class TeamRecruitForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '모집공고 제목을 입력해주세요.'
    }))
    essencial = forms.CharField(widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '지원자격을 입력해주세요.'
    }))
    plus = forms.CharField(widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '우대사항을 입력해주세요.'
    }))
    manpower = forms.CharField(widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '모집 인원 수를 입력해주세요.'
    }))
    career = forms.CharField(widget=forms.Select(choices=CAREERS, attrs={
        'required':'required'
    }))
    contact_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '모집 담당자 이름을 입력해주세요.'
    }))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '모집 담당자 전화번호를 입력해주세요.'
    }))
    contact_email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'team_input',
        'placeholder': '모집 담당자 이메일주소를 입력해주세요.'
    }))
    class Meta:
        model = FindMember
        field = '__all__'
        exclude = ('team',)


class RegisterRequestForm(forms.ModelForm):
    class Meta:
        model = RegisteredMember
        field = '__all__'
        exclude = ('user','team','status',)