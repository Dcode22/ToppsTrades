from django.shortcuts import render, redirect
from profiles.models import Sale, Bid
from .models import Card

# Create your views here.
def home(request):
    sales = Sale.objects.all()
    return render(request, "home.html", {'sales': sales})

def sell(request, profile_id, card_id):
    Sale.objects.create(profile_id=profile_id, card_id=card_id)
    return redirect('profile')

def bid(request, sale_id):
    sales = request.user.profile.sales.all()
    cards_for_sale = [] 
    for sale in sales:
        cards_for_sale.append(sale.card)

    offers = request.user.profile.bids.all()
    cards_offered= []
    for offer in offers:
        cards_offered.append(offer.card)

    sale= Sale.objects.get(id=sale_id)

    content = {
        "cards_for_sale": cards_for_sale, 
        "cards_offered": cards_offered,
        'sale': sale
        }
    return render(request, "bid.html", content)

def offer(request, sale_id, card_id):
    sale = Sale.objects.get(id=sale_id)
    card = Card.objects.get(id=card_id)
    offer = Bid.objects.create(profile_id=request.user.profile.id, sale_id=sale_id, card_id=card_id)
    return render(request, "offer.html", {'sale':sale, 'card':card, 'offer':offer})


def myoffers(request):

    return render(request, 'myoffers.html')



def mysales(request):
    return render(request, 'mysales.html')

def deleteSale(request, sale_id):
    Sale.objects.filter(id=sale_id).delete()
    return render(request, 'mysales.html')

def deleteOffer(request, bid_id):
    Bid.objects.filter(id=bid_id).delete()
    return render(request, 'myoffers.html')