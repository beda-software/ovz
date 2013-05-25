# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from models import ProfessionsLetter
from play_and_learn.mixins import ProfessionsNavigateMixin


class LetterList(ProfessionsNavigateMixin, ListView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/professions/letters.html'
    context_object_name = 'letters'

    def get_breadcrumb_list(self):
        return [
            (u'Играем и учимся', reverse('play_and_learn')),
            (u'Азбука профессий', reverse('play_and_learn.letter_list'))
        ]


class ProfessionList(ProfessionsNavigateMixin, DetailView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/professions/professions.html'
    context_object_name = 'letter'
    slug_field = 'letter_slug'

    def get_breadcrumb_list(self):
        return [
            (u'Играем и учимся', reverse('play_and_learn')),
            (u'Азбука профессий', reverse('play_and_learn.letter_list')),
            (self.object.letter.upper(), reverse('play_and_learn.profession_list', None, (), {
                'slug': self.object.letter_slug
            }))
        ]
