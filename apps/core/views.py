from django.shortcuts import render, redirect, get_object_or_404
from apps.teams.models import *
from apps.member.models import *
from apps.teams.forms import *
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
        print('업데이트 시작')
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
def team_recruit(request, team_pk):
    posting_type = "create"
    team = get_object_or_404(Team, pk=team_pk)
    if request.method == 'POST':
        form = TeamRecruitForm(request.POST, request.FILES)
        if form.is_valid():
            newRecruit = form.save(commit=False)
            newRecruit.team = team
            newRecruit.save()
            form.save_m2m()

            return redirect('core:main_page')
    else:
        form = TeamRecruitForm()
    context = {
        'team':team,
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findmate/recruit.html', context)

@login_required
def update_recruit(request, recruit_pk):
    posting_type = "update"
    recruit = get_object_or_404(FindMember, pk=recruit_pk)
    team = recruit.team
    if request.method == 'POST':
        form = TeamRecruitForm(request.POST, request.FILES, instance=recruit)
        if form.is_valid():
            newRecruit = form.save(commit=False)
            newRecruit.team = team
            newRecruit.save()
            form.save_m2m()

            return redirect('core:main_page')
    else:
        print('업데이트 페이지 진입')
        form = TeamRecruitForm(instance=recruit)
    context = {
        'team':team,
        'recruit':recruit,
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findmate/recruit.html', context)


# 팀 디테일 페이지
@login_required
def team_detail(request, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    team_org = TeamOrg.objects.filter(team=team_pk)
    context = {
        'team':team,
        'team_org':team_org,
    }
    return render(request, 'findteam/team_detail.html', context)


# 팀 가입 신청 페이지
@login_required
def team_register_reqeust(request, team_pk):
    posting_type = "create"
    team = get_object_or_404(Team, pk=team_pk)
    if request.method == 'POST':
        form = RegisterRequestForm(request.POST, request.FILES)
        if form.is_valid():
            newRecruit = form.save(commit=False)
            newRecruit.team = team
            newRecruit.save()
            form.save_m2m()

            return redirect('core:main_page')
    else:
        form = RegisterRequestForm()
    context = {
        'team':team,
        'form':form,
        'posting_type':posting_type,
    }
    return render(request, 'findteam/team_register.html', context)