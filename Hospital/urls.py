from django.urls import path
from . import views

#przekierowania do odpowiednich funkcji
urlpatterns = [
    path('home/', views.home),
    path('myappointment/', views.appointment)
]