# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from main.mixins import MainNavigateMixin

__author__ = 'jackdevil'


class YourChoiceNavigateMixin(MainNavigateMixin):
    navbar_active = 'your_choice'

    def get_breadcrumb_list(self):
        return [
            (u'Твой выбор', reverse('your_choice.list')),
        ]
