# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from xhtml2pdf import pisa
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse

from .models import CV


def download_cv_pdf(request, cv_id):
    cv = get_object_or_404(CV, pk=cv_id)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=%s_%s.pdf" % (cv.first_name, cv.last_name)

    html = render_to_string("cv/cv_pdf.html", {
        "cv": cv,
        "MEDIA_ROOT": settings.MEDIA_ROOT,
        "STATIC_ROOT": settings.STATIC_ROOT,
    })
    
    pdf = pisa.pisaDocument(
        StringIO(html.encode("UTF-8")),
        response,
        encoding="UTF-8",
    )
    
    return response