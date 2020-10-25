from django.db import models

# Create your models here.
class Card(models.Model):
    name= models.CharField(max_length= 100)
    position= models.CharField(max_length= 30)
    weight= models.IntegerField()
    height_ft= models.IntegerField()
    height_in= models.IntegerField()
    jersey_number= models.CharField(max_length=30, null=True, blank= True)
    bats= models.CharField(max_length=30)
    throws= models.CharField(max_length=30)
    birth_date= models.DateTimeField()
    team= models.ForeignKey("Team", on_delete=models.CASCADE)
    player_id= models.IntegerField(unique= True)
    

class Team(models.Model):
    name= models.CharField(max_length= 100)
    mlb_id= models.CharField(max_length= 100, unique= True)

