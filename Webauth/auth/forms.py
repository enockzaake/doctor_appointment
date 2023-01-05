from django import forms 

from django.contrib.auth.forms import UserCreationForm

from users.models import Doctor,Patient

class DoctorSignUpForm(UserCreationForm):
    specialization=forms.CharField(max_length=20)
    email=forms.EmailField()
    class Meta:
        model=Doctor
        fields=['username','first_name','last_name','specialization','email','password1','password2']


class PatientSignUpForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=Patient
        fields=['username','first_name','last_name','email','password1','password2']
