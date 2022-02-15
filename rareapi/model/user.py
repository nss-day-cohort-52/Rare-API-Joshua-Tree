from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class rareUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    created_on = models.DateField(auto_now=False, auto_now_add=False)