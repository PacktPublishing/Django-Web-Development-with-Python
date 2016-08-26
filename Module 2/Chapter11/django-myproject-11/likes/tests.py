# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import unittest
import mock
import json
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from locations.models import Location


class JSSetLikeViewTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(JSSetLikeViewTest, cls).setUpClass()
        cls.location = Location.objects.create(
            title="Haus der Kulturen der Welt",
            slug="hkw",
            small_image="locations/2015/11/20151116013056_small.jpg",
            medium_image="locations/2015/11/20151116013056_medium.jpg",
            large_image="locations/2015/11/20151116013056_large.jpg",
        )
        cls.content_type = ContentType.objects.get_for_model(Location)
        cls.username = "test-admin"
        cls.password = "test-admin"
        cls.superuser = User.objects.create_superuser(
            username=cls.username,
            password=cls.password,
            email="",
        )

    @classmethod
    def tearDownClass(cls):
        super(JSSetLikeViewTest, cls).tearDownClass()
        cls.location.delete()
        cls.superuser.delete()

    def test_authenticated_js_set_like(self):
        from .views import json_set_like
        mock_request = mock.Mock()
        mock_request.user = self.superuser
        mock_request.method = "POST"
        response = json_set_like(mock_request, self.content_type.pk, self.location.pk)
        result = json.loads(response.content)
        self.assertTrue("obj" in result)

    def test_anonymous_js_set_like(self):
        from .views import json_set_like
        mock_request = mock.Mock()
        mock_request.user.is_authenticated.return_value = False
        mock_request.method = "POST"
        response = json_set_like(mock_request, self.content_type.pk, self.location.pk)
        result = json.loads(response.content)
        self.assertEqual(result, False)
