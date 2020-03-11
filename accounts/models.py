from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=254, blank=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    mobile_number = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.email + " (" + self.first_name + " " + self.last_name + ")"
