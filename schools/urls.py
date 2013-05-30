# -*- coding: utf-8 -*-
__author__ = 'jackdevil'

from django.conf.urls.defaults import patterns, include, url
from views import List, Detail

urlpatterns = patterns(
    '',
    url(r'^$', List.as_view(), name='schools.list'),
    url(r'^(?P<slug>\S+)/$', Detail.as_view(), name='schools.detail'),
)
