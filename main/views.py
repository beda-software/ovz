# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from main.mixins import MainNavigateMixin


class MainView(MainNavigateMixin, TemplateView):
    template_name = 'main.html'
