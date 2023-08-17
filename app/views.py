from django.shortcuts import render, redirect
from app.models import GalleryImage
from paypalrestsdk import Payment
from django.conf import settings
# Create your views here.

def home(request):
    return render ( request , 'index.html' )

def about(request):
    return render ( request , 'about.html' )

def sermons(request):
    return render(request, 'sermons.html')

def events(request):
    return render(request, 'events.html')

def ministry(request):
    return render(request, 'ministries.html')

def contact(request):
    return render(request, 'contact.html')

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})




def paypal_donation(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        payment = Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "transactions": [{
                "amount": {"total": amount, "currency": "USD"},
            }],
            "redirect_urls": {
                "return_url": f"{settings.BASE_URL}/donation/success/",
                "cancel_url": f"{settings.BASE_URL}/donation/cancel/"
            }
        })

        if payment.create():
            approval_url = [
                link.href for link in payment.links if link.rel == "approval_url"
            ][0]
            return redirect(approval_url)
    return render(request, 'donation.html')

from django.shortcuts import render

def donation_success(request):
    # You might want to update the following logic based on your needs
    transaction_id = request.GET.get('paymentId')  # Get PayPal payment ID
    # Process and save the transaction details in your database if needed

    return render(request, 'donation_success.html')


def donation_cancel(request):
    return render(request, 'donation_cancel.html')

