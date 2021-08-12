from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = "api"

urlpatterns = [
    path('notice_list/<str:team_pk>', notice_list, name="notice_list"),
    path('notice_detail/<str:notice_pk>', notice_detail, name="notice_detail"),
    path('notice_update/<str:notice_pk>', notice_update, name="notice_update"),
]