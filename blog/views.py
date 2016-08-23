from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Weave
from .models import KeratinBond
from .models import MicroRing
from .models import TapedHairExtention
from .models import MakeUp
from .models import Lash_Brow
from .models import Nail
from .models import Hairdressing
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm

from .forms import MyForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def hair_extentions(request):
    Weaves = Weave.objects.all()
    KeratinBonds = KeratinBond.objects.all()
    MicroRings = MicroRing.objects.all()
    TapedHairExtentions = TapedHairExtention.objects.all()
    return render(request, 'blog/hair_extentions.html', {'Weaves': Weaves,'KeratinBonds': KeratinBonds, 'MicroRings': MicroRings, 'TapedHairExtentions': TapedHairExtentions })
	
def make_up(request):
    MakeUps = MakeUp.objects.all()
    return render(request, 'blog/make_up.html', {'MakeUps': MakeUps})
	
def lashes_brows(request):
    Lashes_Brows = Lash_Brow.objects.all()
    return render(request, 'blog/lashes_brows.html', {'Lashes_Brows': Lashes_Brows})
	
def nails(request):
    Nails = Nail.objects.all()
    return render(request, 'blog/nails.html', {'Nails': Nails})

def hairdressing(request):
    Hairdressings = Hairdressing.objects.all()
    return render(request, 'blog/hairdressing.html', {'Hairdressings': Hairdressings})
	
def contact(request):
    return render(request, 'blog/contact.html')
		
def price_list(request):
    # What you want the button to do.
    Weaves = Weave.objects.all()
    KeratinBonds = KeratinBond.objects.all()
    MicroRings = MicroRing.objects.all()
    TapedHairExtentions = TapedHairExtention.objects.all()
    MakeUps = MakeUp.objects.all()
    Lashes_Brows = Lash_Brow.objects.all()
    Nails = Nail.objects.all()
    Hairdressings = Hairdressing.objects.all()
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10.00",
        "currencycode": "GBP",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "blog/price_list.html", {'Weaves': Weaves, 'KeratinBonds': KeratinBonds, 'MicroRings': MicroRings, 'TapedHairExtentions': TapedHairExtentions, 'MakeUps': MakeUps, 'Lashes_Brows': Lashes_Brows, 'Nails': Nails, 'Hairdressings': Hairdressings})
	
