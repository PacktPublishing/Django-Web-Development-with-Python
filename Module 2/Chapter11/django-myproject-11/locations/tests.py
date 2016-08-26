# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from time import sleep
from django.test import LiveServerTestCase
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from likes.models import Like
from .models import Location


class LiveLocationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(LiveLocationTest, cls).setUpClass()
        cls.browser = webdriver.Firefox()
        cls.browser.delete_all_cookies()
        cls.location = Location.objects.create(
            title="Haus der Kulturen der Welt",
            slug="hkw",
            small_image="locations/2015/11/20151116013056_small.jpg",
            medium_image="locations/2015/11/20151116013056_medium.jpg",
            large_image="locations/2015/11/20151116013056_large.jpg",
        )
        cls.username = "test-admin"
        cls.password = "test-admin"
        cls.superuser = User.objects.create_superuser(
            username=cls.username,
            password=cls.password,
            email="",
        )

    @classmethod
    def tearDownClass(cls):
        super(LiveLocationTest, cls).tearDownClass()
        cls.browser.quit()
        cls.location.delete()
        cls.superuser.delete()

    def test_login_and_like(self):
        # login
        self.browser.get("%(website)s/admin/login/?next=/locations/%(slug)s/" % {
            "website": self.live_server_url,
            "slug": self.location.slug,
        })
        username_field = self.browser.find_element_by_id("id_username")
        username_field.send_keys(self.username)
        password_field = self.browser.find_element_by_id("id_password")
        password_field.send_keys(self.password)
        self.browser.find_element_by_css_selector('input[type="submit"]').click()
        WebDriverWait(self.browser, 10).until(
            lambda x: self.browser.find_element_by_css_selector('.like-button')
        )
        # click on the "like" button
        like_button = self.browser.find_element_by_css_selector('.like-button')
        is_initially_active = "active" in like_button.get_attribute("class")
        initial_likes = int(self.browser.find_element_by_css_selector('.like-badge').text)

        sleep(2)

        like_button.click()
        WebDriverWait(self.browser, 10).until(
            lambda x: int(self.browser.find_element_by_css_selector('.like-badge').text) != initial_likes
        )
        likes_in_html = int(self.browser.find_element_by_css_selector('.like-badge').text)
        likes_in_db = Like.objects.filter(
            content_type=ContentType.objects.get_for_model(Location),
            object_id=self.location.pk,
        ).count()

        sleep(2)

        self.assertEqual(likes_in_html, likes_in_db)
        if is_initially_active:
            self.assertLess(likes_in_html, initial_likes)
        else:
            self.assertGreater(likes_in_html, initial_likes)

        # click on the "like" button again to switch back to the previous state
        like_button.click()
        WebDriverWait(self.browser, 10).until(
            lambda x: int(self.browser.find_element_by_css_selector('.like-badge').text) == initial_likes
        )

        sleep(2)
