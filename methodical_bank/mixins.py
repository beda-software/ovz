# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from main.mixins import MainNavigateMixin

__author__ = 'jackdevil'


class MethodicalBankNavigateMixin(MainNavigateMixin):
    navbar_active = 'methodical_bank'

    def get_breadcrumb_list(self):
        return [
            (u'Методическая копилка', reverse('metodical_bank.list')),
        ]
