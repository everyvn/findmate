from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('<int:pk>', MemberInfo.as_view(), name='member_info'),

]