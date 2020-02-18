from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=100, )
    role = models.CharField(max_length=100, blank=False)
    profilepic = models.ImageField(upload_to='team-profilepics', blank=True)
    github = models.URLField(max_length=1000, blank=True)
    linkedIn = models.URLField(max_length=1000, blank=True)
    twitter = models.URLField(max_length=1000, blank=True)
    dribble = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.team + ' - ' + self.role
