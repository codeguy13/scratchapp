from django.contrib.auth.models import User
from django.db import models

class registrations(models.Model):
    TRUCK_REG_NUMBER = models.IntegerField()