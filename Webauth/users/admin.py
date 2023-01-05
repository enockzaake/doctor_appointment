from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Doctor,Patient,Appointment
from users.models import CustomUser

   
class DoctorAdmin(UserAdmin):   
    pass
    #list_display=['first_name','last_name','email','password','specialization']

class PatientAdmin(UserAdmin):
    pass
    

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment)

