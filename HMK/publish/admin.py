from django.contrib import admin
from django import forms
from .models import PlayerSecurity, Player

class PlayerSecurityAdminForm(forms.ModelForm):

    class Meta:
        model = PlayerSecurity
        fields = '__all__'


class PlayerSecurityAdmin(admin.ModelAdmin):
    form = PlayerSecurityAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(PlayerSecurity, PlayerSecurityAdmin)


class PlayerAdminForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'


class PlayerAdmin(admin.ModelAdmin):
    form = PlayerAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'data']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'data']

admin.site.register(Player, PlayerAdmin)


