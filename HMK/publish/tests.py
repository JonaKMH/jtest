import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import PlayerSecurity, Player
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_playersecurity(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return PlayerSecurity.objects.create(**defaults)


def create_player(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["data"] = "data"
    defaults.update(**kwargs)
    if "security" not in defaults:
        defaults["security"] = create_playersecurity()
    return Player.objects.create(**defaults)


class PlayerSecurityViewTest(unittest.TestCase):
    '''
    Tests for PlayerSecurity
    '''
    def setUp(self):
        self.client = Client()

    def test_list_playersecurity(self):
        url = reverse('publish_playersecurity_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_create_playersecurity(self):
    #     url = reverse('publish_playersecurity_create')
    #     data = {
    #         "name": "name",
    #     }
    #     response = self.client.post(url, data=data)
    #     self.assertEqual(response.status_code, 302)

    def test_detail_playersecurity(self):
        playersecurity = create_playersecurity()
        url = reverse('publish_playersecurity_detail', args=[playersecurity.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_playersecurity(self):
        playersecurity = create_playersecurity()
        data = {
            "name": "name",
        }
        url = reverse('publish_playersecurity_update', args=[playersecurity.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PlayerViewTest(unittest.TestCase):
    '''
    Tests for Player
    '''
    def setUp(self):
        self.client = Client()

    def test_list_player(self):
        url = reverse('publish_player_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_create_player(self):
    #     url = reverse('publish_player_create')
    #     data = {
    #         "name": "name",
    #         "data": "data",
    #         "security": create_playersecurity().pk,
    #     }
    #     response = self.client.post(url, data=data)
    #     self.assertEqual(response.status_code, 302)

    def test_detail_player(self):
        player = create_player()
        url = reverse('publish_player_detail', args=[player.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_update_player(self):
    #     player = create_player()
    #     data = {
    #         "name": "name",
    #         "data": "data",
    #         "security": create_playersecurity().pk,
    #     }
    #     url = reverse('publish_player_update', args=[player.slug,])
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, 302)


