from django import forms

from .models import Post
from .models import Weave
from .models import Weave_Price
from .models import KeratinBond
from .models import KeratinBond_Price
from .models import MicroRing
from .models import MicroRing_Price
from .models import TapedHairExtention
from .models import TapedHairExtention_Price
from .models import Pricee

DISPLAY_CHOICES = (
    ("hairextentionsbox", "hairextentions"),
    ("makeupbox", "makeup")
)

class MyForm(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)