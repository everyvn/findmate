from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = "core"

urlpatterns = [
    # 팀 관련
    path('team_delete/<str:team_pk>/', team_delete, name="team_delete"),
    path('team_management/<str:team_pk>/', team_management, name="team_management"),
    path('team_register_reqeust/<str:team_pk>/', team_register_reqeust, name="team_register_reqeust"),
    path('team_detail/<str:team_pk>/', team_detail, name="team_detail"),
    path('update_team/<str:team_pk>/', update_team, name="update_team"),
    path('make_team/', make_team, name="make_team"),
    path('team_select/', team_select, name="team_select"),
    # 멤버 관련
    path('update_recruit/<str:recruit_pk>/', update_recruit, name="update_recruit"),
    path('team_recruit/<str:team_pk>/', team_recruit, name="team_recruit"),
    path('members/', member_list, name="member_list"),
    path('', main_page, name="main_page"),
]