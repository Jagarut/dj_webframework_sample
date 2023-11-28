from django.shortcuts import render
from . import models
# Create your views here.
def profiles(request):
    profiles = models.Profile.objects.all()
    context = {
        "profiles": profiles,
    }
    return render(request, "users/profiles.html", context )
    # return render(request, models.UserProfile, name="profiles" )