from django.db import models


class Dashboard(models.Model):
    event_name = models.CharField(max_length=100, blank=True)
    starts_on = models.DateTimeField()
    action = models.booleanField(default=True)
