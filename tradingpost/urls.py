from django.urls import path
from . import views

urlpatterns= [
    path('home/', views.home, name="homepage"),
    path('sell/<int:profile_id>/<int:card_id>/', views.sell, name='sell'),
    path('bid/<int:sale_id>/', views.bid, name='bid'),
    path('offer/<int:sale_id>/<int:card_id>/', views.offer, name='offer'),
    path('myoffers/', views.myoffers, name='myoffers'),
    path('mysales/', views.mysales, name='mysales'),
    path('deletesale/<int:sale_id>', views.deleteSale, name='deletesale'),
    path('deleteoffer/<int:bid_id>', views.deleteOffer, name='deleteoffer')

]