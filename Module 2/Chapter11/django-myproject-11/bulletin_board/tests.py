# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Bulletin


class BulletinTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(BulletinTests, cls).setUpClass()
        cls.superuser, created = User.objects.get_or_create(
            username="admin",
        )
        cls.superuser.is_active = True
        cls.superuser.is_superuser = True
        cls.superuser.save()

        cls.category = Category.objects.create(title="Movies")

        cls.bulletin = Bulletin.objects.create(
            bulletin_type="searching",
            category=cls.category,
            title="The Matrix",
            description="There is no Spoon.",
            contact_person="Aidas Bendoraitis",
        )
        cls.bulletin_to_delete = Bulletin.objects.create(
            bulletin_type="searching",
            category=cls.category,
            title="Animatrix",
            description="There is no Spoon.",
            contact_person="Aidas Bendoraitis",
        )

    @classmethod
    def tearDownClass(cls):
        super(BulletinTests, cls).tearDownClass()
        cls.category.delete()
        cls.bulletin.delete()
        cls.superuser.delete()

    def test_list_bulletins(self):
        url = reverse("rest_bulletin_list")
        data = {}
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], Bulletin.objects.count())
        
    def test_get_bulletin(self):
        url = reverse("rest_bulletin_detail", kwargs={"pk": self.bulletin.pk})
        data = {}
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.bulletin.pk)

    def test_create_bulletin_allowed(self):
        self.client.force_authenticate(user=self.superuser)  # login
        url = reverse("rest_bulletin_list")
        data = {
            "bulletin_type": "offering",
            "category": {"title": self.category.title},
            "title": "Back to the Future",
            "description": "Roads? Where we're going, we don't need roads.",
            "contact_person": "Aidas Bendoraitis",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(response.data["id"], self.bulletin.pk)
        self.client.force_authenticate(user=None)  # logout

    def test_create_bulletin_restricted(self):
        self.client.force_authenticate(user=None)  # make sure the user is logged out
        url = reverse("rest_bulletin_list")
        data = {
            "bulletin_type": "offering",
            "category": {"title": self.category.title},
            "title": "Back to the Future",
            "description": "Roads? Where we're going, we don't need roads.",
            "contact_person": "Aidas Bendoraitis",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_change_bulletin_allowed(self):
        self.client.force_authenticate(user=self.superuser)  # login
        url = reverse("rest_bulletin_detail", kwargs={"pk": self.bulletin.pk})
        data = {
            "bulletin_type": self.bulletin.bulletin_type,
            "category": {"title": self.bulletin.category.title},
            "title": "Matrix Resurrection",  # change only title
            "description": self.bulletin.description,
            "contact_person": self.bulletin.contact_person,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.bulletin.pk)
        self.assertEqual(response.data["bulletin_type"], "searching")
        self.client.force_authenticate(user=None)  # logout

    def test_change_bulletin_restricted(self):
        self.client.force_authenticate(user=None)  # make sure the user is logged out
        url = reverse("rest_bulletin_detail", kwargs={"pk": self.bulletin.pk})
        data = {
            "bulletin_type": self.bulletin.bulletin_type,
            "category": {"title": self.bulletin.category.title},
            "title": "Matrix Resurrection",  # change only title
            "description": self.bulletin.description,
            "contact_person": self.bulletin.contact_person,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_bulletin_allowed(self):
        self.client.force_authenticate(user=self.superuser)  # login
        url = reverse("rest_bulletin_detail", kwargs={"pk": self.bulletin_to_delete.pk})
        data = {}
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.force_authenticate(user=None)  # logout

    def test_delete_bulletin_restricted(self):
        self.client.force_authenticate(user=None)  # make sure the user is logged out
        url = reverse("rest_bulletin_detail", kwargs={"pk": self.bulletin_to_delete.pk})
        data = {}
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
