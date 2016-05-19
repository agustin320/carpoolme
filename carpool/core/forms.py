from django import forms
from core.models import Pool


class PoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ('origen', 'destino', 'tipo', 'dias', 'fecha', 'hora', 'contacto_email', 'contacto_telefono')


class SearchForm(forms.Form):
    origen = forms.CharField(max_length=60)
    destino = forms.CharField(max_length=60)
