from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
#create your views here
def home(request):
  return HttpResponse('<h1>Home Page</h1>')

def about(request):
  return render(request, 'about.html')
