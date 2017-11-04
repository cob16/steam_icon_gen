from django import forms
from django.core.validators import MinValueValidator


class ShortcutForm(forms.Form):
    appid = forms.IntegerField(label='App id', required=True, validators=[
            MinValueValidator(0)
        ])
    name = forms.CharField(label='Name', max_length=100, required=True)
