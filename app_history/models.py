from django.db import models


class History(models.Model):
    ip = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.ip} {self.region}"
