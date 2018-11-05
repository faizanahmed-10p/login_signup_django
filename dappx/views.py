from django.shortcuts import render
from dappx.forms import UserForm,VoterProfileInfoForm, CandidateProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dappx.models import CandidateProfileInfo, CandidateVote
from dappx.helper import server, districtGenerator
import requests
import json
from django.core import serializers


def index(request):
    return render(request,'dappx/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = VoterProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            fullName = str(user.first_name)+str(user.last_name)
            voter_profile = {
                    "$class" : "org.ecp.voting.voter", 
                    "voterID":  user.username,
                    "fullName" : str(fullName),
                    "gender" : str(profile.gender)
            }
            ifVoted_data = {
                 "$class": "org.ecp.voting.ifVoted",
                 "voterID": user.username,
                 "votedOrNot": "false"
            }
            print(voter_profile)

            requests.post(server+'/api/voter', json = voter_profile)
            requests.post(server+'/api/ifVoted', json = ifVoted_data)

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = VoterProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def candidate_register(request):
    registered = False
    constituency_list = []
    i=0
    contituency = requests.get(server+'/api/district').json()
    while(i < len(contituency)):
        constituency_list.append(( contituency[i]["districtName"] ))
        i= i+1
    political_parties = requests.get(server+'/api/politicalParty').json()
    print(political_parties)
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = CandidateProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.constituency = request.POST['const']
            profile.party = request.POST['party'] 
            profile.save()
            fullName = str(user.first_name)+str(user.last_name)
            district_url = server+'/api/queries/filterDistrictByName?nameParam={}'.format(request.POST['const'])
            url = server+'/api/queries/PartyByNames?partyParam={}'.format(request.POST['party'])
            district_info = requests.get(district_url).json()
            political_party_data = requests.get(url).json()
            candidate_vote_id_data = CandidateVote.objects.create(candidate_id= str(user.username))
            candidateVoteId = str(candidate_vote_id_data.candidate_vote_id)
            candidate_data = {
                "$class": "org.ecp.voting.candidate",
                "candidateID": str(user.username),
                "fullName": fullName,
                "party": political_party_data[0],
                "IndependentStatus": "false"
            }
            candidate_vote_data = {
                "$class": "org.ecp.voting.candidateVote",
                "candidateVoteId": candidateVoteId,
                "totalVote": "0",
                "candidateProfile": json.dumps(candidate_data),
                "candidateDistrict": district_info[0]
            }           
            candidate_payload = json.dumps(candidate_data)
            print(candidate_vote_data)
            print(requests.post(server+'/api/candidate', json = candidate_data))
            requests.post(server+'/api/candidate', json = candidate_data)
            print(requests.post(server+'/api/candidateVote', json = candidate_vote_data))
            requests.post(server+'/api/candidateVote', json = candidate_vote_data)
            registered = True


        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = CandidateProfileInfoForm()
    return render(request,'dappx/candidate_registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'constituencies':constituency_list,
                           'parties': political_parties})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})


def ballot_box(request):
    voted = False
    political_parties = requests.get(server+'/api/politicalParty')
    resp = political_parties.json()
    if request.user.is_authenticated:
        print(request.user.username)
        contituency = districtGenerator(request.user.username)
        contituency_name = str(contituency['districtName'])
        print(contituency_name)
        constituency_candidates = CandidateProfileInfo.objects.filter(constituency=contituency_name)
        print(constituency_candidates)
    if request.method == 'POST':
        voted=True


    else:
        print(type(resp))
        #payload = political_parties.json()
        payload = {
            "candidate1" : {
                "first_name" : "org.ecp.voting.voter", 
                "party":  "4220117774685",
            },
            "candidate2" : {
                "first_name" : "org.ecp", 
                "party":  "223656545",
            }
        }
        #data = json.loads(payload)
    return render(request,'dappx/ballot.html' , { 'candidates' : constituency_candidates })