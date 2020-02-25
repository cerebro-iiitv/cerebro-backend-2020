from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Event(models.Model):
    event = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=2000, blank=True)
    prize = models.CharField(max_length=20, blank=True)
    team_size = models.IntegerField()
    venue = models.CharField(max_length=50, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rule1 = models.CharField(max_length=500, blank=False)
    rule2 = models.CharField(max_length=500, blank=False)
    rule3 = models.CharField(max_length=500, blank=False)
    rule4 = models.CharField(max_length=500, blank=True)
    rule5 = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='event-images/', null=True, blank=True)

    def __str__(self):
        return self.event


class Contact(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=40)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name + ' (' + self.role + ')'


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    token = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.token
