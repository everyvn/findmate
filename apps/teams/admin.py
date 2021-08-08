from django.contrib import admin
from .models import Team, RegisteredMember, FindMember, TeamOrg
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

class TeamOrgAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions','indented_title','parent','user','position')

admin.site.register(Team)
admin.site.register(RegisteredMember)
admin.site.register(FindMember)
admin.site.register(TeamOrg, TeamOrgAdmin)



