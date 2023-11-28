from django.shortcuts import render
from . import models
# Create your views here.
def profiles(request):
    return render(request, "users/profiles.html" )
    # return render(request, models.UserProfile, name="profiles" )