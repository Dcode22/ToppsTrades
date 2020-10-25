from django.contrib.auth import login, authenticate, update_session_auth_hash
from .models import Profile, Card, Sale, Bid
from .forms import SignUpForm, EditProfileForm, EditUserForm
from django.shortcuts import render, redirect
import random
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile= Profile.objects.create(user=user)
            cards= random.sample(list(Card.objects.all()), k=10)
            profile.cards_owned.add(*cards)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):

    sales = request.user.profile.sales.all()
    cards_for_sale = [] 
    for sale in sales:
        cards_for_sale.append(sale.card)

    offers = request.user.profile.bids.all()
    cards_offered= []
    for offer in offers:
        cards_offered.append(offer.card)

    content = {
        "cards_for_sale": cards_for_sale, 
        "cards_offered": cards_offered
        }

    return render(request, 'profile.html', content)


def editProfile(request):
    if request.method == 'POST':
        form1 = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        form2 = EditUserForm(data=request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
        # update.user = request.user
        return redirect('profile')
    else:
        form1 = EditProfileForm(instance=request.user.profile)
        form2 = EditUserForm(instance=request.user)


    return render(request, 'edit_profile.html', {'form1': form1, 'form2': form2})


def rejectOffer(request, offer_id):
    Bid.objects.filter(id=offer_id).delete()
    # still have to notify bidder
    return redirect('mysales')


def acceptOffer(request, offer_id):
    offer = Bid.objects.get(id=offer_id)
    offer.sale.profile.cards_owned.add(offer.card)
    offer.profile.cards_owned.add(offer.sale.card)
    offer.profile.cards_owned.remove(offer.card)
    offer.sale.profile.cards_owned.remove(offer.sale.card)
    offer.sale.delete()
    return redirect('mysales')

