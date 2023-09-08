from django.db import models


class UserData(models.Model):
    user_name = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    date_time = models.CharField(max_length=200, blank=True, null=True)
