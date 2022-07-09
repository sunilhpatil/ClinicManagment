from statistics import mode
from django.db import models

# Create your models here.

class Country(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    Id = models.IntegerField(primary_key=True)
    Country_Name = models.CharField(max_length = 100, unique=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, 
    default='UTC')

    def __str__(self):
        return self.Country_Name


'''Oranization Detaills'''
class Organization(models.Model):
    id = models.BigAutoField(primary_key=True)
    Org_Code = models.CharField(max_length=5)ß
    Org_Name = models.CharField(max_length=100)
    Org_ShortName = models.CharField(max_length=10)
    Country_Code = models.ForeignKey(Country, on_delete=models.RESTRICT)

    def __str__(self):
        return self.Org_Name

