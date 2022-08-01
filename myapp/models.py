from django.db import models

# Create your models here.
class Country(models.Model):
    # Representing Many to one relationships between Country and city
    # Specifying the country parent model class
    country = models.CharField(max_length=100, null=False)
    def __str__(self):
        return (self.country)


class Population(models.Model):
    # Creating Datamodel to  store different populations of different city
    country= models.ForeignKey(Country, null = True,on_delete = models.CASCADE)
    # Specifying one two many relationships using Foreign key
    city = models.CharField(max_length=100,)
    child_population = models.BigIntegerField()
    man_population = models.BigIntegerField()
    woman_population = models.BigIntegerField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return (self.city)