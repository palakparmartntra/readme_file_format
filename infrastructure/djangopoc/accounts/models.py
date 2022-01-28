from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from infrastructure.djangopoc.accounts.constants import GENDER


class User(AbstractUser):
    """ user model for auth"""
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
