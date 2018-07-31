from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import PlayerSecurity, Player
from .forms import PlayerSecurityForm, PlayerForm


class PlayerSecurityListView(ListView):
    model = PlayerSecurity


class PlayerSecurityCreateView(CreateView):
    model = PlayerSecurity
    form_class = PlayerSecurityForm


class PlayerSecurityDetailView(DetailView):
    model = PlayerSecurity


class PlayerSecurityUpdateView(UpdateView):
    model = PlayerSecurity
    form_class = PlayerSecurityForm


class PlayerListView(ListView):
    model = Player


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm


class PlayerDetailView(DetailView):
    model = Player


class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm

