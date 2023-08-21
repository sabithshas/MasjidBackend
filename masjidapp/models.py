from django.db import models

# Create your models here.
class Countries(models.Model):
    countryname=models.CharField(max_length=200)
    countrycode=models.CharField(max_length=100)
    def __str__(self):
        return self.countryname

class States(models.Model):
    statename=models.CharField(max_length=200)
    state_code=models.CharField(max_length=100)
    countrycode=models.ForeignKey(Countries,on_delete=models.CASCADE)
    def __str__(self):
        return self.statename
    
class District(models.Model):
    districtname=models.CharField(max_length=200)
    district_code=models.CharField(max_length=100)
    state_code=models.ForeignKey(States,on_delete=models.CASCADE)
    def __str__(self):
        return self.districtname

class Masjidregister(models.Model):
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    aliasname=models.CharField(max_length=400)
    address=models.CharField(max_length=300)
    def __str__(self):
        return self.name