# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateResponseMixin

__author__ = 'jackdevil'


class NavigateTemplateMixin(TemplateResponseMixin):
    navbar = []
    navbar_active = 'main'
    breadcrumb_list = []

    def get_breadcrumb_list(self):
        return self.breadcrumb_list

    def get_navbar(self):
        return [
            {'name': 'main', 'description': u'Главная', 'url': reverse('main')},
            {'name': 'play_and_learn', 'description': u'Играем и учимся', 'url': reverse('play_and_learn')},
        ]

    def get_navbar_active(self):
        return self.navbar_active

    def render_to_response(self, context, **response_kwargs):
        self.request.navbar = self.get_navbar()
        self.request.navbar_active = self.get_navbar_active()
        self.request.breadcrumbs(self.get_breadcrumb_list())
        return super(NavigateTemplateMixin, self).response_class(
            request=self.request, template=self.get_template_names(),
            context=context, **response_kwargs)