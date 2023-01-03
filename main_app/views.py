from django.shortcuts import render
from .models import Climb


# Define the home view
#create your views here
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def climbs_index(request):
  climbs=Climb.objects.all()
  return render(request, 'climbs/index.html', { 'climbs': climbs })