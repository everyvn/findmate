from django.shortcuts import render, redirect, get_object_or_404
from apps.teams.models import *
from apps.member.models import *
from apps.teams.forms import TeamRegisterForm, TeamRecruitForm
from django.contrib.auth.decorators import login_required
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

@login_required
def make_team(request):
    posting_type = "create"
    if request.method == 'POST':
        form = TeamRegisterForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            newTeam = form.save(commit=False)
            newTeam.save()
            form.save_m2m()

            return redirect('core:main_page')
    else:
        form = TeamRegisterForm()
    context = {
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findteam/maketeam.html', context)

@login_required
def update_team(request, team_pk):
    posting_type = "update"
    team = get_object_or_404(Team, pk=team_pk)
    if request.method == 'POST':
        form = TeamRegisterForm(request.POST, request.FILES, instance=team)
        print(form)
        if form.is_valid():
            print('The form is valid')
            newTeam = form.save(commit=False)
            newTeam.save()
            form.save_m2m()

            return redirect('core:main_page')
    else:
        form = TeamRegisterForm(instance=team)
    context = {
        'team':team,
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findteam/maketeam.html', context)

@login_required
def team_select(request):
    teams = get_object_or_404(Profile, user=request.user).teams.all()
    context = {
        'teams':teams,
    }
    return render(request, 'findmate/select_team.html', context)

@login_required
def team_recruit(request):
    posting_type = "create"
    if request.method == 'POST':
        form = TeamRecruitForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            newTeam = form.save(commit=False)
            newTeam.save()
            form.save_m2m()

            return redirect('core:main_page')
    else:
        form = TeamRecruitForm()
    context = {
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findmate/recruit.html', context)

@login_required
def update_recruit(request, recruit_pk):
    posting_type = "update"
    team = get_object_or_404(Team, pk=team_pk)
    if request.method == 'POST':
        print('업데이트 시작', posting_type, team)
        form = TeamRegisterForm(request.POST, request.FILES, instance=team)
        print(form)
        if form.is_valid():
            print('The form is valid')
            newTeam = form.save(commit=False)
            newTeam.save()
            form.save_m2m()

            return redirect('core:main_page')
    else:
        print('업데이트 페이지 진입')
        form = TeamRegisterForm(instance=team)
    context = {
        'team':team,
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findmate/recruit.html', context)