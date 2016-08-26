# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import xlwt

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse

from .models import Product, ProductPhoto


class ProductPhotoInline(admin.StackedInline):
    model = ProductPhoto
    extra = 0


def export_xls(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = "attachment; filename=products.xls"
    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Products")

    row_num = 0

    columns = [
        ("ID", 2000),
        ("Title", 6000),
        ("Description", 8000),
        ("Price (€)", 3000),
        ("Preview", 10000),
    ]

    header_style = xlwt.XFStyle()
    header_style.font.bold = True

    for col_num, (item, width) in enumerate(columns):
        ws.write(row_num, col_num, item, header_style)
        # set column width
        ws.col(col_num).width = width

    text_style = xlwt.XFStyle()
    text_style.alignment.wrap = 1

    price_style = xlwt.XFStyle()
    price_style.num_format_str = "0.00"

    styles = [text_style, text_style, text_style, price_style, text_style]

    for obj in queryset.order_by("pk"):
        row_num += 1
        project_photos = obj.productphoto_set.all()[:1]
        url = ""
        if project_photos:
            url = "http://{0}{1}".format(
                request.META['HTTP_HOST'],
                project_photos[0].photo.url,
            )
        row = [
            obj.pk,
            obj.title,
            obj.description,
            obj.price,
            url,
        ]
        for col_num, item in enumerate(row):
            ws.write(row_num, col_num, item, styles[col_num])

    wb.save(response)
    return response

export_xls.short_description = _("Export XLS")


class PhotoFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("photos")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "photos"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ("zero", _("Has no photos")),
            ("one", _("Has one photo")),
            ("many", _("Has more than one photo")),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        qs = queryset.annotate(
            num_photos=models.Count("productphoto")
        )
        if self.value() == "zero":
            qs = qs.filter(num_photos=0)
        elif self.value() == "one":
            qs = qs.filter(num_photos=1)
        elif self.value() == "many":
            qs = qs.filter(num_photos__gte=2)
        return qs


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "get_photo", "price"]
    list_editable = ["price"]
    list_filter = [PhotoFilter]

    fieldsets = (
        (_("Product"), {"fields": ("title", "slug", "description", "price")}),
    )

    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductPhotoInline]
    actions = [export_xls]

    def get_photo(self, obj):
        project_photos = obj.productphoto_set.all()[:1]
        if project_photos:
            return """<a href="%(product_url)s" target="_blank">
                <img src="%(photo_url)s" alt="" width="100" />
            </a>""" % {
                "product_url": obj.get_url_path(),
                "photo_url":  project_photos[0].photo.url,
            }
        return ""
    get_photo.short_description = _("Preview")
    get_photo.allow_tags = True


admin.site.register(Product, ProductAdmin)
