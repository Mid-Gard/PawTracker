from django.urls import path
from . import views

urlpatterns = [
    path('', views.driver_details)
] #providing a url to the site