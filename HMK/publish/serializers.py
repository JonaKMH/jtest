from . import models

from rest_framework import serializers


class PlayerSecuritySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlayerSecurity
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Player
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'data', 
        )


