from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

class Doctor(CustomUser):
    specialization=models.CharField(max_length=20)
    about=models.CharField(max_length=100,default='No info')
    
    class Meta:
        verbose_name='DOCTOR'
        verbose_name_plural='DOCTORS'

    def short_about(self):
        return self.about[:30] + '...'
    @property
    def is_patient(self):
        return True

    def __str__(self) -> str:
        return self.get_full_name()
    
class Patient(CustomUser):
    
    class Meta:
        verbose_name='PATIENT'
        verbose_name_plural='PATIENTS'

    @property
    def is_doctor(self):
        return True
        
    def __str__(self) -> str:
        return self.get_full_name() 


class Appointment(models.Model):
    patient=models.ForeignKey(Patient,related_name='patient',on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,related_name='doctor',on_delete=models.CASCADE)
    issue=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.patient.get_full_name()











