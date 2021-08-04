from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = "core"

urlpatterns = [
    # 팀 관련
    path('make_team/', make_team, name="make_team"),
    path('update_team/<str:team_pk>/', update_team, name="update_team"),
    # 멤버 관련
    path('members/', member_list, name="member_list"),
    path('', main_page, name="main_page"),
]