from django import forms
from .models import PlayerSecurity, Player


class PlayerSecurityForm(forms.ModelForm):
    class Meta:
        model = PlayerSecurity
        fields = ['name']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'data', 'security']


