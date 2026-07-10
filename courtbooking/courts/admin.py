from django.contrib import admin
from .models import Court, Booking, Sport, Coach, Activity

# Register your models here.
admin.site.register(Court)
admin.site.register(Booking)
admin.site.register(Sport)
admin.site.register(Coach)
admin.site.register(Activity)