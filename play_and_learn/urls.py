# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from views import LetterList, ProfessionList


urlpatterns = patterns(
    '',
    url(r'^$', LetterList.as_view(), name='play_and_learn'),
    url(r'^letter_list/$', LetterList.as_view(), name='play_and_learn.letter_list'),
    url(r'^letter/(?P<slug>\S{1,3})/$', ProfessionList.as_view(), name='play_and_learn.profession_list'),
)
