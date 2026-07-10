from django.contrib import admin
from .models import Court, Booking, Sport, Coach

# Register your models here.
admin.site.register(Court)
admin.site.register(Booking)
admin.site.register(Sport)
admin.site.register(Coach)