from rest_framework import serializers
from events.models import Event, Contact


class EventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
