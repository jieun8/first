from django import forms
from .models import Pockemon
from .widgets import GoogleMapPointWidget


class PockemonForm(forms.ModelForm):
    class Meta:
        model = Pockemon
        fields = '__all__'
        widgets = {
            'lnglat': GoogleMapPointWidget,
        }