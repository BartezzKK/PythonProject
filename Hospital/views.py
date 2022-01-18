from email import message
from multiprocessing import context
from django.shortcuts import render, redirect



def home(request):
    return render(request, 'home.html')

def appointment(request):
    if request.user.is_authenticated:
        return render(request, 'myappointment.html', {})
    else:
        return redirect('/home')
