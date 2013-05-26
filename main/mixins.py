# -*- coding: utf-8 -*-
from collections import OrderedDict
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateResponseMixin

__author__ = 'jackdevil'


class NavigateTemplateMixin(TemplateResponseMixin):
    navbar = []
    navbar_active = None
    sub_navbar = []
    sub_navbar_active = None
    breadcrumb_list = []

    def get_navbar(self):
        return self.navbar

    def get_navbar_active(self):
        return self.navbar_active

    def get_sub_navbar(self):
        navbar = self.get_navbar()
        navbar_active = self.get_navbar_active()
        if not self.sub_navbar and 'sub_navbar' in navbar[navbar_active]:
            self.sub_navbar = navbar[navbar_active]['sub_navbar']
        return self.sub_navbar

    def get_sub_navbar_active(self):
        return self.sub_navbar_active

    def get_breadcrumb_list(self):
        return self.breadcrumb_list

    def render_to_response(self, context, **response_kwargs):
        self.request.navbar = self.get_navbar()
        self.request.navbar_active = self.get_navbar_active()
        self.request.sub_navbar = self.get_sub_navbar()
        self.request.sub_navbar_active = self.get_sub_navbar_active()
        if self.get_breadcrumb_list():
            self.request.breadcrumbs(self.get_breadcrumb_list())
        return self.response_class(
            request=self.request, template=self.get_template_names(),
            context=context, **response_kwargs)


class MainNavigateMixin(NavigateTemplateMixin):
    navbar_active = 'main'

    def get_navbar(self):
        return OrderedDict(((
            'main', {
                'description': u'Главная',
                'url': reverse('main')
            }),(
            'play_and_learn', {
                'description': u'Играем и учимся',
                'url': reverse('play_and_learn'),
                'sub_navbar': OrderedDict((
                    (
                        'professions', {
                            'description': u'Азбука профессий',
                            'url': reverse('play_and_learn.letter_list')
                        }
                    ),(
                        'game', {
                            'description': u'Профигротека',
                            'url': '#'
                        }
                    )
                ))
            }),(
            'your_choice', {
                'description': u'Твой выбор',
                'url': '#'
            }),(
            'schools', {
                'description': u'Учебные заведения',
                'url': '#'
            }),(
            'labor_market', {
                'description': u'Рынок труда',
                'url': '#'
            }),(
            'methodical_bank', {
                'description': u'Методическая копилка',
                'url': '#'
            }),(
            'guest', {
                'description': u'Гостевая',
                'url': '#'
            })
        ))