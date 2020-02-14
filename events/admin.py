from django.contrib import admin
from events.models import Event, Participant, Contact

admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(Participant)
