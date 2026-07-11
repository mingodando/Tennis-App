from django.contrib import admin
from .models import (
    Sport, Court, Coach, Activity, ActivityBooking,
    AddOn, BookingAddOn, Booking, Payment, UserProfile,
    TimeSlot, CheckIn, CoachAvailability
)


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'hourly_rate', 'is_active')
    list_filter = ('sport', 'is_active')
    search_fields = ('name',)


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'hourly_rate', 'is_active')
    list_filter = ('sport', 'is_active')
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'coach', 'date', 'price', 'max_participants', 'is_active')
    list_filter = ('sport', 'is_active', 'date')
    search_fields = ('name',)


@admin.register(ActivityBooking)
class ActivityBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'participant_count', 'total_price', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'activity__name')


@admin.register(AddOn)
class AddOnAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'price', 'is_active')
    list_filter = ('sport', 'is_active')
    search_fields = ('name',)


@admin.register(BookingAddOn)
class BookingAddOnAdmin(admin.ModelAdmin):
    list_display = ('booking', 'add_on', 'quantity', 'subtotal')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'court', 'start_time', 'end_time', 'status')
    list_filter = ('court', 'status')
    search_fields = ('user__username',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username', 'transaction_id')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'member_id', 'phone', 'joined_date')
    search_fields = ('member_id', 'phone', 'user__username')


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('court', 'date', 'start_time', 'end_time', 'is_blocked', 'reason')
    list_filter = ('court', 'is_blocked')


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ('booking', 'checked_in_at', 'checked_in_by', 'status')
    list_filter = ('status',)


@admin.register(CoachAvailability)
class CoachAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('coach', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('coach', 'day_of_week')