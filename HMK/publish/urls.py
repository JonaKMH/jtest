from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'playersecurity', api.PlayerSecurityViewSet)
router.register(r'player', api.PlayerViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for PlayerSecurity
    url(r'^publish/playersecurity/$', views.PlayerSecurityListView.as_view(), name='publish_playersecurity_list'),
    url(r'^publish/playersecurity/create/$', views.PlayerSecurityCreateView.as_view(), name='publish_playersecurity_create'),
    url(r'^publish/playersecurity/detail/(?P<slug>\S+)/$', views.PlayerSecurityDetailView.as_view(), name='publish_playersecurity_detail'),
    url(r'^publish/playersecurity/update/(?P<slug>\S+)/$', views.PlayerSecurityUpdateView.as_view(), name='publish_playersecurity_update'),
)

urlpatterns += (
    # urls for Player
    url(r'^publish/player/$', views.PlayerListView.as_view(), name='publish_player_list'),
    url(r'^publish/player/create/$', views.PlayerCreateView.as_view(), name='publish_player_create'),
    url(r'^publish/player/detail/(?P<slug>\S+)/$', views.PlayerDetailView.as_view(), name='publish_player_detail'),
    url(r'^publish/player/update/(?P<slug>\S+)/$', views.PlayerUpdateView.as_view(), name='publish_player_update'),
)

