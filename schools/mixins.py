# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from main.mixins import MainNavigateMixin

__author__ = 'jackdevil'


class SchoolNavigateMixin(MainNavigateMixin):
    navbar_active = 'schools'

    def get_breadcrumb_list(self):
        return [
            (u'Учебные заведения', reverse('schools.list')),
        ]
