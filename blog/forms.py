from django import forms

from .models import Post
from .models import Weave
from .models import KeratinBond
from .models import MicroRing
from .models import TapedHairExtention



DISPLAY_CHOICES = (
    ("hairextentionsbox", "hairextentions"),
    ("makeupbox", "makeup")
)

class MyForm(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)