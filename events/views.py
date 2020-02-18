from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from events.models import Event, Contact, Participant
from events.serializers import EventSerializers, ParticipantSerializers, ContactSerializers


class EventViewSets(ModelViewSet):
    serializer_class = EventSerializers
    queryset = Event.objects.all()


class ContactViewSets(ModelViewSet):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()


class ParticipantViewSets(ModelViewSet):
    serializer_class = ParticipantSerializers
    queryset = Participant.objects.all()
