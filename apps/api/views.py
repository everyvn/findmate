from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FindMemberList
from apps.teams.models import FindMember, Team
# Create your views here.

# teams페이지 팝업창 내 모집공고 리스트 불러오기
@api_view(['GET'])
def notice_list(request, team_pk):
    team = get_object_or_404(Team, pk = team_pk)
    notices = FindMember.objects.filter(team = team)
    serializer = FindMemberList(notices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def notice_detail(request, notice_pk):
    notice = get_object_or_404(FindMember, pk = notice_pk)
    serializer = FindMemberList(notice)
    return Response(serializer.data)