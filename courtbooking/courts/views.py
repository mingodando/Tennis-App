from django.shortcuts import render
from .models import Court
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.shortcuts import render, redirect
from .models import Activity, Coach
from datetime import datetime, timedelta



def court_list(request):
    courts = Court.objects.filter(is_active=True)
    return render(request, "courts/court_list.html", {
        "courts": courts,
        "user": request.user,
    })

@login_required #Required login to view the page
def edit_profile(request):
    profile = request.user.userprofile  #Gets the profile

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("courts:court-list")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "courts/edit_profile.html", {"form": form})

def activity_list(request):
    activities = Activity.objects.filter(is_active=True)
    return render(request, "courts/activity_list.html", {"activities": activities})


def coach_list(request):
    coaches = Coach.objects.filter(is_active=True)
    return render(request, "courts/coach_list.html", {"coaches": coaches})

