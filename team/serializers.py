from rest_framework import serializers
from team.models import Team


class TeamSerializers(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
