from django.shortcuts import render
from dappx.forms import UserForm,VoterProfileInfoForm, CandidateProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dappx.models import CandidateProfileInfo
from dappx.helper import get_json_format
import requests
import json


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
    data = {
    "$class" : "org.ecp.voting.voter", 
    "voterID":  "4220117774685",
    "fullName" : "faizan ahmed",
    "gender" : "male"
    }
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
            #json_object =  get_json_format(user_form, profile_form)
            #resp = requests.get('')
            #print(resp)
            registered = True
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
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = CandidateProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #print(user_form.cleaned_data.get('first_name') + profile_form.cleaned_data.get('id'))
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            print(profile.save())
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = CandidateProfileInfoForm()
    return render(request,'dappx/candidate_registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


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
    #if request.method == 'POST':

    
    political_parties = requests.get('https://a4d79848.ngrok.io/api/politicalParty')
    resp = political_parties.json()
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
    return render(request,'dappx/ballot.html' , { 'candidates' : resp })