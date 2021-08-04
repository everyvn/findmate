from django.shortcuts import render, redirect
from apps.teams.models import *
from apps.member.models import *
from apps.teams.forms import TeamRegisterForm
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
    posting_type = "create"
    if request.method == 'POST':
        form = TeamRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            newTeam = form.save(commit=False)
            newTeam.save()
            form.save_m2m()

            return redirect('core:team_list')

    else:
        form = TeamRegisterForm()
    
    context = {
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findteam/maketeam.html', context)