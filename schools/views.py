# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from models import School
from mixins import SchoolNavigateMixin


class List(SchoolNavigateMixin, ListView):
    model = School
    template_name = 'schools/list.html'
    context_object_name = 'schools'


class Detail(SchoolNavigateMixin, DetailView):
    model = School
    template_name = 'schools/detail.html'
    context_object_name = 'school'

    def get_breadcrumb_list(self):
        breadcrumb_list = super(Detail, self).get_breadcrumb_list()
        breadcrumb_list.append(
            (self.object.name, reverse('schools.detail', None, (), {
                'slug': self.object.slug
            }))
        )
        return breadcrumb_list