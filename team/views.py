from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from team.models import Team
from team.serializers import TeamSerializers


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializers
    queryset = Team.objects.all()
