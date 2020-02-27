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
    pdf = models.FileField(upload_to='pdf/', null=True, blank=True)

    def __str__(self):
        return self.event


class Contact(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    convenor = models.CharField(max_length=100, blank=False)
    role1 = models.CharField(max_length=40)
    phone_number1 = PhoneNumberField(blank=True)

    co_convenor1 = models.CharField(max_length=100, blank=False)
    role2 = models.CharField(max_length=40)
    phone_number2 = PhoneNumberField(blank=True)

    co_convenor2 = models.CharField(max_length=100, blank=True)
    role3 = models.CharField(max_length=40, blank=True)
    phone_number3 = PhoneNumberField(blank=True)

    member1 = models.CharField(max_length=100, blank=False)
    role4 = models.CharField(max_length=40)

    member2 = models.CharField(max_length=100, blank=False)
    role5 = models.CharField(max_length=40)

    def __str__(self):
        return str(self.pk)
