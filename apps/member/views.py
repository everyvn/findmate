from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import DetailView
# Create your views here.

class MemberInfo(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'member_info/member_info.html'