# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from haystack.views import SearchView


class CrispySearchView(SearchView):
    def extra_context(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.disable_csrf = True
        return {"search_helper": helper}

admin.autodiscover()

login_helper = FormHelper()
login_helper.form_action = reverse_lazy("my_login_page")
login_helper.form_method = "POST"
login_helper.form_class = "form-signin"
login_helper.html5_required = True

login_helper.layout = layout.Layout(
    layout.HTML(string_concat("""<h2 class="form-signin-heading">""", _("Please Sign In"), """</h2>""")),
    layout.Field("username", placeholder=_("username")),
    layout.Field("password", placeholder=_("password")),
    layout.HTML("""<input type="hidden" name="next" value="{{ next }}" />"""),
    layout.Submit("submit", _("Login"), css_class="btn-lg"),
)


urlpatterns = i18n_patterns('',
    url(r'login/$', 'django.contrib.auth.views.login', {'extra_context': {'login_helper': login_helper}}, name="my_login_page"),
    url(r'^email-messages/', include("email_messages.urls")),
    url(r'^quotes/', include("quotes.urls")),
    url(r'^bulletin-board/', include("bulletin_board.urls")),
    url(r'^movies/', include("movies.urls")),
    url(r'^cv/', include("cv.urls")),
    url(r'^search/$', CrispySearchView(), name='haystack_search'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
