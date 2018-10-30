from django.contrib import admin
from dappx.models import VoterProfileInfo, User, CandidateProfileInfo
# Register your models here.
admin.site.register(VoterProfileInfo)
admin.site.register(CandidateProfileInfo)