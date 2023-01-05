from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('doctordashboard/',views.doctordashboard,name='doctordashboard'),
    path('patientdashboard/',views.patientdashboard,name='patientdashboard'),
    path('appointment/<doc_id>/<p_id>/',views.appointment,name='appointment'),
    path('doc/<id>',views.doc,name='doc')
]














