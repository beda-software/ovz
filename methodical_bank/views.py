# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from models import MethodicalBank
from mixins import MethodicalBankNavigateMixin


class List(MethodicalBankNavigateMixin, ListView):
    model = MethodicalBank
    template_name = 'methodical_bank/list.html'
    context_object_name = 'letters'


class Detail(MethodicalBankNavigateMixin, DetailView):
    model = MethodicalBank
    template_name = 'methodical_bank/detail.html'
    context_object_name = 'metodic'

    def get_breadcrumb_list(self):
        breadcrumb_list = super(Detail, self).get_breadcrumb_list()
        breadcrumb_list.append(
            (self.object.name, reverse('metodical_bank.detail', None, (), {
                'slug': self.object.slug
            }))
        )
        return breadcrumb_list