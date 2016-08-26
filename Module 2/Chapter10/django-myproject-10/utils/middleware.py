# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from threading import local
_thread_locals = local()


def get_current_request():
    """ returns the HttpRequest object for this thread """
    return getattr(_thread_locals, "request", None)


def get_current_user():
    """ returns the current user if it exists, otherwise returns None """
    request = get_current_request()
    if request:
        return getattr(request, "user", None)


class ThreadLocalMiddleware(object):
    """ Middleware that adds the HttpRequest object to thread local storage."""
    def process_request(self, request):
        _thread_locals.request = request