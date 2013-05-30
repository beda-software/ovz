# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from main.mixins import MainNavigateMixin

__author__ = 'jackdevil'


class PlayAndLearnNavigateMixin(MainNavigateMixin):
    navbar_active = 'play_and_learn'

    def get_breadcrumb_list(self):
        return [
            (u'Играем и учимся', reverse('play_and_learn')),
        ]


class ProfessionsNavigateMixin(PlayAndLearnNavigateMixin):
    sub_navbar_active = 'professions'

    def get_breadcrumb_list(self):
        breadcrumb_list = super(ProfessionsNavigateMixin, self).get_breadcrumb_list()
        breadcrumb_list.append(
            (u'Азбука профессий', reverse('play_and_learn.letter_list'))
        )
        return breadcrumb_list
