from django.shortcuts import render
from .models import Court

# Create your views here.

def court_list(request):
    courts = Court.objects.filter(is_active=True)
    return render(request, "courts/court_list.html", {"courts": courts})
