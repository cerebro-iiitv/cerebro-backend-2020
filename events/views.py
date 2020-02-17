from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from events.models import Event, Contact, Participant
from events.serializers import EventSerializers, ParticipantSerializers, ContactSerializers


class EventViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializers
    queryset = Event.objects.all()


class ContactViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()


class ParticipantViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ParticipantSerializers
    queryset = Participant.objects.all()
