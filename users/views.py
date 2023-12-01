from django.shortcuts import render
from . import models
# Create your views here.
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