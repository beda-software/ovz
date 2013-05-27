# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from models import ProfessionsLetter
from play_and_learn.mixins import ProfessionsNavigateMixin


class LetterList(ProfessionsNavigateMixin, ListView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/professions/letters.html'
    context_object_name = 'letters'


class ProfessionList(ProfessionsNavigateMixin, DetailView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/professions/professions.html'
    context_object_name = 'letter'
    slug_field = 'letter_slug'

    def get_breadcrumb_list(self):
        breadcrumb_list = super(ProfessionList, self).get_breadcrumb_list()
        breadcrumb_list.append(
            (self.object.letter.upper(), reverse('play_and_learn.profession_list', None, (), {
                'slug': self.object.letter_slug
            }))
        )
        return breadcrumb_list