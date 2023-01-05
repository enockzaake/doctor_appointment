from django.urls import path

from . import views

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('doctorregister/',views.doctor_register,name='doctorregister'),
    path('patientregister/',views.patient_register,name='patientregister'),
]

