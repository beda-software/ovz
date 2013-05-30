# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from views import TotalInfoList, JobList


urlpatterns = patterns(
    '',
    url(r'^$', TotalInfoList.as_view(), name='labor_market'),
    url(r'^total_info/$', TotalInfoList.as_view(), name='labor_market.total_info'),
    url(r'^job/$', JobList.as_view(), name='labor_market.job'),
)
