from multiprocessing import context
from django.shortcuts import render, redirect




def home(request):
    return render(request, 'home.html')

def appointment(request):
    return render(request, 'myappointment.html')
