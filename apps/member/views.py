from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.

def member_info(request):
    profile = get_object_or_404(Profile, user = request.user)
    context = {
        'profile':profile,
    }
    return render(request, 'member_info/member_info.html', context)