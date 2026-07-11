from django.shortcuts import render
from .models import Court, Booking
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.shortcuts import render, redirect
from .models import Activity, Coach
from datetime import datetime, timedelta
from django.utils import timezone as django_timezone



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

@login_required
def book_court(request, court_id):
    court = Court.objects.get(id=court_id)

    if request.method == "POST":
        date = request.POST.get("date")
        start_time_str = request.POST.get("start_time")
        duration = int(request.POST.get("duration"))

        naive_start = datetime.strptime(f"{date} {start_time_str}", "%Y-%m-%d %H:%M")
        start_time = django_timezone.make_aware(naive_start)
        end_time = start_time + timedelta(minutes=duration)

        Booking.objects.create(
            user=request.user,
            court=court,
            start_time=start_time,
            end_time=end_time,
        )
        return redirect("courts:court-list")

    return render(request, "courts/book_court.html", {"court": court})