from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from . import models
from .forms import CustomUserCreationForm
# Create your views here.

def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("profiles") 

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exits!")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or password is incorrect!")

    return render(request, "users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.error(request, "User was logout!")
    return redirect('login')

def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)   #saves the form data to create a new user instance but doesn't commit (save) it to the database immediately
            # It's a common practice to standardize usernames to prevent case-related issues during authentication or to enforce a specific format.
            user.username = user.username.lower()
            user.save() #commits (saves) the modified user object to the database.

            messages.success(request, "User account was created")

            login(request, user)
            return redirect("profiles")
        
        else:
            messages.success(request, "An error has ocurred during registration")


    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)

def profiles(request):
    profiles = models.Profile.objects.all()
    context = {
        "profiles": profiles,
    }
    return render(request, "users/profiles.html", context )

def user_profile(request, pk):
    profile = models.Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        "profile": profile,
        "topSkills": topSkills,
        "otherSkills": otherSkills,
    }
    return render(request, "users/user-profile.html", context )