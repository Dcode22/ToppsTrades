from django.db import models
from django.contrib.auth.models import User 
from tradingpost.models import Card

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/avatar.png", upload_to="profile_pics")
    # coins = models.IntegerField(default=1000)
    cards_owned = models.ManyToManyField(Card)

class Sale(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sales")
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="bids")
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='bids')
    created = models.DateTimeField(auto_now_add=True)

