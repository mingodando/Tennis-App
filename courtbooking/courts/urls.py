from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path("", views.court_list, name="court-list"),
    path("profile/edit/", views.edit_profile, name="edit-profile"),
    path("activities/", views.activity_list, name="activity-list"),
    path("coaches/", views.coach_list, name="coach-list"),
    path("<int:court_id>/book/", views.book_court, name="book-court"),
    path("activities/<int:activity_id>/register/", views.register_activity, name="register-activity"),
    path("coaches/<int:coach_id>/book/", views.book_coach, name="book-coach"),
]