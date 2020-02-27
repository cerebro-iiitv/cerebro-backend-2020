from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from events.models import Event, Contact
from events.serializers import EventSerializers, ContactSerializers


class EventViewSets(ModelViewSet):
    serializer_class = EventSerializers
    queryset = Event.objects.all()


class ContactViewSets(ModelViewSet):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()
