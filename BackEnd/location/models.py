from django.db import models

# Create your models here.

class Bus1_data(models.Model):
    # bus1_lat, bus1_lng, bus1_bearing
    bus1_lat = models.FloatField()
    bus1_lng = models.FloatField()
    bus1_time = models.TextField()
    bus1_date = models.TextField()
    bus1_speed = models.FloatField()

    def __str__(self):
        return "Bus1_Coordinates"

class Bus2_data(models.Model):

    bus2_lat = models.FloatField()
    bus2_lng = models.FloatField()
    bus2_time = models.TextField()
    bus2_date = models.TextField()
    bus2_speed = models.FloatField()

    def __str__(self):
        return "Bus2_Coordinates"

class Bus3_data(models.Model):

    bus3_lat = models.FloatField()
    bus3_lng = models.FloatField()
    bus3_time = models.TextField()
    bus3_date = models.TextField()
    bus3_speed = models.FloatField()

    def __str__(self):
        return "Bus3_Coordinates"

class Bus4_data(models.Model):
    bus4_lat = models.FloatField()
    bus4_lng = models.FloatField()
    bus4_time = models.TextField()
    bus4_date = models.TextField()
    bus4_speed = models.FloatField()
    
    def __str__(self):
        return "Bus4_Coordinates"