from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns= [
    path('profile/', views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
    path('editprofile/', views.editProfile, name="edit_profile"),
    path('changepassword/', views.change_password, name="change_password"),
    path('sfsdf6979702/<int:offer_id>/', views.rejectOffer, name="reject_offer"),
    path('khu0344bv8i3/<int:offer_id>/', views.acceptOffer, name="accept_offer")
]