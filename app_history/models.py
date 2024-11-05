from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class History(models.Model):
    ip = models.CharField(max_length=50)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ip} {self.region}"


class Users(models.Model):
    login = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user_name}"

    def __unicode__(self):
        return self.login

