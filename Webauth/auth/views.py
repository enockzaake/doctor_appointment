from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


from .forms import DoctorSignUpForm,PatientSignUpForm

def doctor_register(request):
    form=DoctorSignUpForm()
    if request.method == 'POST':
        form=DoctorSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('login')
    return render(request,'doctorregister.html',{'form':form})

def patient_register(request):
    form=PatientSignUpForm()
    if request.method == 'POST':
        form=PatientSignUpForm(request.POST)
        print('valid.................. 1')
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()
            print('valid..................')
            return redirect('login')
        else:
            messages.success(request,form.errors)    

    return render(request,'patientregister.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')        
        user=authenticate(username=email,password=password)
        if user is not None:
            print('not none')
            if user.is_active:
                login(request,user)
                messages.success(request,'LOGIN SUCCESSFUL')
                return redirect('index')
    return render(request,'login.html',{})


def user_logout(request):
    logout(request)
    messages.success(request,'You were logged out.')
    return redirect('login')
