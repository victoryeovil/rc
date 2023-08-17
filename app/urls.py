from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('sermons/', sermons, name='sermons'),
    path('events/', events, name='events'),
    path('ministry/', ministry, name='ministry'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery_view, name='gallery'),

    path('donation/', paypal_donation, name='donation'),
    # Define other URLs here
    path('donation/success/', donation_success, name='donation_success'),
    path('donation/cancel/', donation_cancel, name='donation_cancel'),
]
