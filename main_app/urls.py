from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for climbs index
    path('climbs/', views.climbs_index, name='index'),
    path('climbs/<int:climb_id>/', views.climbs_detail, name='detail'),
]


