from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor,Patient,Appointment
from .forms import AppointmentForm
import datetime

def index(request):
    doctors=Doctor.objects.all()
    return render(request,'index.html',{'doctors':doctors})


@login_required(login_url='login')
def doctordashboard(request):
    return render(request,'doctordashboard.html',{})

@login_required(login_url='login')
def patientdashboard(request):
    doctors=Doctor.objects.all()
    return render(request,'patientdashboard.html',{'doctors':doctors})

@login_required(login_url='login')
def appointment(request,doc_id,p_id):

    form=AppointmentForm()
    doctor=Doctor.objects.get(id=doc_id)
    if request.method == 'POST':
        doctor=Doctor.objects.get(id=doc_id)
        patient=Patient.objects.get(id=p_id)
        issue=request.POST['issue']
        date=request.POST['date']
        date=datetime.date.strftime("%m/%d/%y")
        appoint=Appointment.objects.create(issue=issue,doctor=doctor,patient=patient,date=date)
        appoint.save()
        messages.success(request,'Appointment booked succesfully')
        return redirect('patientdashboard')

    return render(request,'appointment.html',{'form':form,'doctor':doctor})
    

def doc(request,id):
    doc=Doctor.objects.get(id=id)
    return render(request,'doc.html',{'doc':doc})