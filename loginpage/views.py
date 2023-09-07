from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.user is not None and request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'home.html')


def about(request):
    params = {
        'name': 'Uzair',
        "age": 23
    }
    return render(request, "about.html", params)


def dashboard(request):
    if request.user and request.user.is_authenticated:
        return render ( request , 'dashboard.html' )
    else:
        messages.warning(request, "Please Login First.")
        return redirect('home')


def handlelogin(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        keepMeLoggedIn = request.POST.get('keepMeLoggedIn')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            if not keepMeLoggedIn:
                request.session.set_expiry(10)
            messages.success(request, "Login Successful.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials X.")
            return redirect('home')
    return HttpResponse('404 - Bad Request')


def handlelogout(request):
    if request.user.is_authenticated:
        messages.info(request,"Logout successful.")
        logout(request)
        return redirect('home')
    else:
        messages.warning(request, "User already logged out. Login first.")
        return redirect('home')

