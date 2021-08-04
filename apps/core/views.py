from django.shortcuts import render
from apps.teams.models import *
from apps.member.models import *
# Create your views here.

def main_page(request):
    teams = Team.objects.all()
    context = {
        'teams':teams,
    }
    return render(request, 'findteam/teams.html', context)


def member_list(request):
    members = Profile.objects.all()
    context = {
        'members':members,
    }
    return render(request, 'findmate/members.html', context)


def make_team(request):
    context ={
        
    }
    return render(request, 'findteam/maketeam.html', context)