from django.urls import path
from . import views
# from climbs.views import ClimbList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for climbs index
    path('climbs/', views.ClimbList.as_view(), name='index'),
    path('climbs/<int:climb_id>/', views.climbs_detail, name='detail'),
    path('climbs/create/', views.ClimbCreate.as_view(), name='climbs_create'),
]


