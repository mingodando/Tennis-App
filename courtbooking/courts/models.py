from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Coaches"

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    max_participants = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"

class ActivityBooking(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    participant_count = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Court(models.Model):
    name = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.court.name} - {self.start_time}"