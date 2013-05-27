# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^play_and_learn/', include('play_and_learn.urls')),
    url(r'^guest/', include('guest.urls')),
    url(r'^methodical_bank/', include('methodical_bank.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
