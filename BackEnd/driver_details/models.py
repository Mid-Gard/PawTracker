from django.db import models


class Driver_Details(models.Model):
    Name = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=12)
    Driver_Pic = models.CharField(max_length=2803)
