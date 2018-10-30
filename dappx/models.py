from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
# Create your models here.
class VoterProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mother = models.CharField(max_length=128)
    father = models.CharField(max_length=128)
    birth_city = models.CharField(max_length=128)
    birth_district = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    date_of_birth = models.DateField(blank=False, default=datetime.now)


class CandidateProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    party = models.CharField(max_length=128)


def __str__(self):
  return self.user.username
