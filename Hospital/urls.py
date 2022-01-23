from django.urls import path
from . import views

#przekierowania do odpowiednich funkcji
urlpatterns = [
    path('home/', views.home, name='home'),
    path('myappointment/', views.appointment),
    path('addDoctor/', views.addDoctorForm),
    path('', views.home)
    
]