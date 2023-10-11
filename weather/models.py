from django.db import models


class Location(models.Model):
    province   = models.CharField(max_length=100)
    country    = models.CharField(max_length=100)
    latitude   = models.DecimalField(max_digits=8, decimal_places=5)
    longtitude = models.DecimalField(max_digits=8, decimal_places=5)    

    def __str__(self):
        return (self.province + ", " + self.country)

