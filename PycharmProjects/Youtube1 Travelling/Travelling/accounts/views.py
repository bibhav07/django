from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.contrib.auth import login,logout

# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password']
        confirmpassword = request.POST['confirm password']

        if password1 == confirmpassword:
            if User.objects.filter(username=user_name).exists():

                messages.info(request,'Username Taken')
                return redirect('accounts:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('accounts:signup')
            else:
                user = User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("POST")
                return redirect('travel:travello')

        else:
            messages.info(request,'Unmatch password')
            return redirect('accounts:signup')
    else:
     return render(request,'accounts/signup.html')



 # navin login method

def login_view(requets):
    if requets.method == "POST":
        username = requets.POST['username']
        password = requets.POST['password']

        user = auth.authenticate(requets,username=username,password=password)
        if user != None:
            auth.login(requets,user)
            return redirect('travel:travello')
        else:
            messages.info(requets,'User Not Avilable Please signup for login!')
            return redirect('accounts:login')
    else:
        return render(requets,'accounts/login.html')




def logout_views(request):
    if request.method == "POST":
        logout(request)
        return redirect('travel:travello')


 #   my login method
# def login_view(request):
#     if request.method == 'POST':
#       form = AuthenticationForm(data=request.POST)
#       if form.is_valid():
#           user = form.get_user()
#           login(request,user)
#
#           if 'next' in request.POST:
#               return redirect(request.POST.get('next'))
#           else:
#               return redirect('travel:travello')
#
#
#     else:
#         form = AuthenticationForm()
#     return render(request,'accounts/login.html',{'form':form})