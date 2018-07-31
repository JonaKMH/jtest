from . import models
from . import serializers
from rest_framework import viewsets, permissions


class PlayerSecurityViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlayerSecurity class"""

    queryset = models.PlayerSecurity.objects.all()
    serializer_class = serializers.PlayerSecuritySerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Player class"""

    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]


