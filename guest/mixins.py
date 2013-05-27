# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from main.mixins import MainNavigateMixin

__author__ = 'jackdevil'


class GuestNavigateMixin(MainNavigateMixin):
    navbar_active = 'guest'

    def get_breadcrumb_list(self):
        return [
            (u'Гостевая', reverse('guest')),
        ]