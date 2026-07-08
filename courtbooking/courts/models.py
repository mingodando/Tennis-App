from django.db import models

# Create your models here.
class Courts(models.Model):
    name = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)