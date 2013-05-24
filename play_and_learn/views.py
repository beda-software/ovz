# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from main.mixins import NavigateTemplateMixin
from models import ProfessionsLetter


class LetterList(NavigateTemplateMixin, ListView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/professions/letters.html'
    context_object_name = 'letters'
    navbar_active = 'play_and_learn'

    def get_breadcrumb_list(self):
        return [
            (u'Играем и учимся', reverse('play_and_learn')),
            (u'Азбука профессий', reverse('play_and_learn.letter_list'))
        ]


class ProfessionList(NavigateTemplateMixin, DetailView):
    model = ProfessionsLetter
    template_name = 'play_and_learn/professions/professions.html'
    context_object_name = 'letter'
    slug_field = 'letter_slug'
    navbar_active = 'play_and_learn'

    def get_breadcrumb_list(self):
        return [
            (u'Играем и учимся', reverse('play_and_learn')),
            (u'Азбука профессий', reverse('play_and_learn.letter_list')),
            (self.object.letter, reverse('play_and_learn.profession_list', None, (), {
                'slug': self.object.letter_slug
            }))
        ]
