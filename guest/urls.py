# -*- coding: utf-8 -*-
__author__ = 'jackdevil'

from django.conf.urls.defaults import patterns, include, url
from views import GuestView, GuestSuccessView

urlpatterns = patterns(
    '',
    url(r'^$', GuestView.as_view(), name='guest'),
    url(r'^success/$', GuestSuccessView.as_view(), name='guest.success'),
)
