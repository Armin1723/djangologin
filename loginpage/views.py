from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    if request.user is not None and request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'home.html')


def about(request):
    return render(request, "about.html")


def dashboard(request):
    if request.user and request.user.is_authenticated:
        return render ( request , 'dashboard.html' )
    else:
        messages.warning(request, "Please Login First.")
        return redirect('home')


def handlelogin(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
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


def handlesignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['signupEmail']
        email=request.POST['signupEmail']
        email2=request.POST.get('signupEmailMatch')
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        pass1=request.POST.get('signupPass')
        pass2=request.POST.get('signupPassMatch')
        houseNo=request.POST.get('houseNo')
        lane=request.POST.get('lane')
        locality=request.POST.get('locality')
        landmark=request.POST.get('landmark')
        zipCode=request.POST.get('zipCode')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')

        # check for errorneous input
          
        if (pass1!= pass2):
             messages.error(request, "Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        myuser = authenticate(username=email, password=pass1)
        messages.success(request, "You have successfully registered yourself at KMC shop.")
        return render(request, 'dashboard.html')

    else:
        return HttpResponse("404 - Not found")

def handlelogout(request):
    if request.user.is_authenticated:
        messages.info(request,"Logout successful.")
        logout(request)
    else:
        messages.warning(request, "User already logged out. Login first.")
    return redirect('home')

