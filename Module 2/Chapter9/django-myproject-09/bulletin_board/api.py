# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from .models import Category, Bulletin


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = "categories"
        fields = ["title"]
        allowed_methods = ["get"]
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "title": ALL,
        }


class BulletinResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, "category", full=True)

    class Meta:
        queryset = Bulletin.objects.all()
        resource_name = "bulletins"
        fields = ["bulletin_type", "category", "title", "description", "contact_person", "phone", "email", "image"]
        allowed_methods = ["get"]
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "bulletin_type": ALL,
            "title": ALL,
            "category": ALL_WITH_RELATIONS,
        }