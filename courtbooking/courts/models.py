from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]

CHECK_IN_STATUS = [
    ('present', 'Present'),
    ('absent', 'Absent')
]

PAYMENT_METHOD_CHOICES = [
    ('card', 'Card'),
    ('promptpay', 'PromptPay'),
]

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
    date = models.DateField()
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
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def save(self, *args, **kwargs):
        self.total_price = self.activity.price * self.participant_count
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.activity.name}"

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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.court.name} - {self.start_time}"

class AddOn(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class BookingAddOn(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    add_on = models.ForeignKey(AddOn, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.add_on.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.add_on.name} x{self.quantity}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    activity_booking = models.ForeignKey(ActivityBooking, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    transaction_id = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}({self.status})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class TimeSlot(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_blocked = models.BooleanField(default=False)
    reason = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.court.name} - {self.date} ({self.start_time} - {self.end_time})"

class CheckIn(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    checked_in_at = models.DateTimeField(auto_now_add=True)
    checked_in_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=CHECK_IN_STATUS, default="present")

    def __str__(self):
        return f"{self.booking} - {self.status}"

class CoachAvailability(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name_plural = "Coach Availabilities"

    def __str__(self):
        return f"{self.coach.name} - {self.day_of_week} ({self.start_time}-{self.end_time})"