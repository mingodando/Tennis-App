from django.db import models

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