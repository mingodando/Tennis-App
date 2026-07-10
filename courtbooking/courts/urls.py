from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path("", views.court_list, name="court-list"),
    path("profile/edit/", views.edit_profile, name="edit-profile"),
]