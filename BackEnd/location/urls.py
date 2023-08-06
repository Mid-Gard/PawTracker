from django.urls import path 
from . import views 
# from . import Temp_views

urlpatterns = [ path('out_campus', views.bus_outcampus), path('in_campus', views.bus_incampus), path('location_dummy', views.bus_location_dummy),
               path('bus_location', views.bus_location)]