from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from courts.models import Booking, ActivityBooking

@login_required
def home(request):
    now = timezone.now()

    upcoming_bookings = Booking.objects.filter(
        user=request.user,
        start_time__gte=now
    ).order_by("start_time")

    upcoming_activity_bookings = ActivityBooking.objects.filter(
        user=request.user,
        activity__start_time__gte=now
    ).order_by("activity__start_time")

    return render(request, "home/home.html", {
        "upcoming_bookings": upcoming_bookings,
        "upcoming_activity_bookings": upcoming_activity_bookings,
    })