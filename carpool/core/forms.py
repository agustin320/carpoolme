from django import forms

from carpool.models import Pool


class PoolForm(forms.ModelForm):

    class Meta:
        model = Pool
        fields = ('email', 'password','origen','destino','tipo','dias','fecha')