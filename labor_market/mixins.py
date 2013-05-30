# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from main.mixins import MainNavigateMixin

__author__ = 'jackdevil'


class LaborMarketNavigateMixin(MainNavigateMixin):
    navbar_active = 'labor_market'

    def get_breadcrumb_list(self):
        return [
            (u'Рынок труда', reverse('labor_market')),
        ]


class TotalInfoNavigateMixin(LaborMarketNavigateMixin):
    sub_navbar_active = 'total_info'


class JobNavigateMixin(LaborMarketNavigateMixin):
    sub_navbar_active = 'job'
