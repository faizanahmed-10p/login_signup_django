from django.contrib import admin
from dappx.models import VoterProfileInfo, User, CandidateProfileInfo, CandidateVote
# Register your models here.
admin.site.register(VoterProfileInfo)
admin.site.register(CandidateProfileInfo)
admin.site.register(CandidateVote)