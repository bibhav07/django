from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# our model

from .models import Destination

# Create your views here.

def travello(request):
    dest = Destination.objects.all()
    return render(request,'index.html',{'dest':dest})


@login_required(login_url='/accounts/login/')
def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def destinations(request):
    return render(request,'destinations.html')


def elements(request):
    return render(request,'elements.html')


def news(request):
    return render(request,'news.html')

