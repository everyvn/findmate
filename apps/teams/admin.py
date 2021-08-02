from django.contrib import admin
from .models import Team, RegisteredMember, FindMember
# Register your models here.
admin.site.register(Team)
admin.site.register(RegisteredMember)
admin.site.register(FindMember)