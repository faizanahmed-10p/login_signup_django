from django import forms
from dappx.models import VoterProfileInfo, CandidateProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    email = forms.EmailField(label  ='Email', widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'xxx@yyy.zzz'}))
    class Meta():
        model = User
        fields = ('username','password','email')

class VoterProfileInfoForm(forms.ModelForm):
    
    CHOICES = (('male', 'Male',), ('female', 'Female',))

    mother = forms.CharField(label="Mother's name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Mother's Name"}))
    father = forms.CharField(label="Father's name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Father's Name"}))
    gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect, choices=CHOICES)
    birth_city = forms.CharField(label="Birth City", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Birth City"}))
    birth_district = forms.CharField(label="Birth District", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Birth District"}))


    class Meta():
        model = VoterProfileInfo
        fields = ('mother' , 'father', 'gender', 'birth_city', 'birth_district')

class CandidateProfileInfoForm(forms.ModelForm):

    CHOICES = (('PPP', 'PPP',), ('MQM', 'Mutahida Qoumi Movement',), ('PTI', 'Pakistan Tehreek-e-Insaf'))
    party = forms.ChoiceField(label='Political Party', widget=forms.RadioSelect, choices=CHOICES)

    class Meta():
        model = CandidateProfileInfo
        fields = ['party']
