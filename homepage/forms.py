from django import forms
from homepage.models import Cow

class CowForm(forms.Form):
    text = forms.CharField(max_length=200)