from django.shortcuts import render
from .models import Climb
from django.views.generic import ListView


# Define the home view
#create your views here
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def climbs_index(request):
#   climbs=Climb.objects.all()
#   return render(request, 'climbs/index.html', { 'climbs': climbs })
class ClimbList(ListView):
  model = Climb
  template_name = 'climbs/index.html'

def climbs_detail(request, climb_id):
  climb = Climb.objects.get(id=climb_id)
  return render(request, 'climbs/detail.html', { 'climb': climb })
