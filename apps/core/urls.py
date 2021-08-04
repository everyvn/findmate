from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('make_team/', make_team, name="make_team"),
    path('members/', member_list, name="team_list"),
    path('', main_page, name="main_page"),
]