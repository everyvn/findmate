from rest_framework import serializers
from apps.teams.models import FindMember

class FindMemberList(serializers.ModelSerializer):
    class Meta:
        model = FindMember
        fields = '__all__'