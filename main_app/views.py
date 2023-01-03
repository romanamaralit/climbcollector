from django.shortcuts import render


# Add the Climb class & list and view function below the imports
class Climb:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, rating, description, location, people):
    self.name = name
    self.rating = rating
    self.description = description
    self.location = location
    self.people = people

climbs = [
  Climb('Change', '5.15c (9b+)', 'Only one person has ever completed this climb.', 'Flatanger, Norway', 1),
  Climb('La Dura Dura', '9b+ (5.15c)', 'Two people have ascended this climb.', 'Peramola, Spain', 2 ),
  Climb('La Rage d’Adam', '9a (5.15d)', 'La rage de dent means toothache', 'Verdon Gorge , France', 0)
]

# Define the home view
#create your views here
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def climbs_index(request):
  return render(request, 'climbs/index.html', { 'climbs': climbs })