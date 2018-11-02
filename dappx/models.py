from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
# Create your models here.
class VoterProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #id = models.CharField(primary_key=True, max_length=128)
    mother = models.CharField(max_length=128)
    father = models.CharField(max_length=128)
    birth_city = models.CharField(max_length=128)
    birth_district = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)


class CandidateProfileInfo(models.Model):
    #id = models.CharField(primary_key=True, max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    party = models.CharField(max_length=128, blank=True)
    independent_status = models.BooleanField(default=False)


def __str__(self):
  return self.user.username
