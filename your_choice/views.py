# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from models import Profession
from mixins import YourChoiceNavigateMixin


class List(YourChoiceNavigateMixin, ListView):
    model = Profession
    template_name = 'your_choice/list.html'
    context_object_name = 'professions'


class Detail(YourChoiceNavigateMixin, DetailView):
    model = Profession
    template_name = 'your_choice/detail.html'
    context_object_name = 'profession'

    def get_breadcrumb_list(self):
        breadcrumb_list = super(Detail, self).get_breadcrumb_list()
        breadcrumb_list.append(
            (self.object.name, reverse('your_choice.detail', None, (), {
                'slug': self.object.slug
            }))
        )
        return breadcrumb_list