from django import forms
from dappx.models import VoterProfileInfo, CandidateProfileInfo
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class UserForm(forms.ModelForm):
    username = forms.CharField(label='CNIC', validators=[RegexValidator('(\d{5}-\d{7}-\d{1})', message="CNIC should be in the format xxxxx-xxxxxxx-x")], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CNIC'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))  
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    email = forms.EmailField(label  ='Email', widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'xxx@yyy.zzz'}))
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

class VoterProfileInfoForm(forms.ModelForm):
    
    CHOICES = (('male', 'Male',), ('female', 'Female',))

    #id = forms.CharField(label="CNIC", validators=[RegexValidator('(\d{5}-\d{7}-\d{1})', message="CNIC should be in the format xxxxx-xxxxxxx-x")], widget=forms.TextInput(attrs={'class':'form-control','placeholder':"CNIC Number"}))
    mother = forms.CharField(label="Mother's name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Mother's Name"}))
    father = forms.CharField(label="Father's name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Father's Name"}))
    gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect, choices=CHOICES)
    birth_city = forms.CharField(label="Birth City", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Birth City"}))
    birth_district = forms.CharField(label="Birth District", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Birth District"}))


    class Meta():
        model = VoterProfileInfo
        fields = ( 'mother' , 'father', 'gender', 'birth_city', 'birth_district')

class CandidateProfileInfoForm(forms.ModelForm):

    CHOICES = (('PPP', 'PPP',), ('MQM', 'Mutahida Qoumi Movement',), ('PTI', 'Pakistan Tehreek-e-Insaf'))

    #id = forms.CharField(label="CNIC", widget=forms.TextInput(attrs={'class':'form-control','placeholder':"CNIC Number"}))
    independent_status = forms.BooleanField(label='Independent Status', required=False)
    party = forms.ChoiceField(label='Political Party', widget=forms.RadioSelect, choices=CHOICES, required=False)


    class Meta():
        model = CandidateProfileInfo
        fields = ( 'party', 'independent_status')

class BallotBox(forms.ModelForm):

    class Meta():
        model = CandidateProfileInfo
        fields = ['party']
