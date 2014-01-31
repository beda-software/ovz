# -*- coding: utf-8 -*-
from collections import OrderedDict
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateResponseMixin
import pytils

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
        return OrderedDict((
            ('main', {
                'description': u'Главная',
                'url': reverse('main')
            }),
            ('play_and_learn', {
                'description': u'Играем и учимся',
                'url': reverse('play_and_learn'),
                'sub_navbar': OrderedDict((
                    ('professions', {
                        'description': u'Азбука профессий',
                        'url': reverse('play_and_learn.letter_list')
                    }),
                    ('game', {
                        'description': u'Профигротека',
                        'url': '#'
                    })
                ))}),
            ('your_choice', {
                'description': u'Твой выбор',
                'url': reverse('your_choice.list')
            }),
            ('schools', {
                'description': u'Учебные заведения',
                'url': reverse('schools.list')
            }),
            ('labor_market', {
                'description': u'Рынок труда',
                'url': reverse('labor_market'),
                'sub_navbar': OrderedDict((
                    ('total_info', {
                        'description': u'Общая информация',
                        'url': reverse('labor_market.total_info')
                    }),
                    ('job', {
                        'description': u'Вакансии',
                        'url': reverse('labor_market.job')
                    })
            ))}),
            ('methodical_bank', {
                'description': u'Методическая копилка',
                'url': reverse('metodical_bank.list')
            }),
            ('guest', {
                'description': u'Гостевая',
                'url': reverse('guest')
            })
        ))

from django.db import models


def create_model(name, fields=None, app_label='', module='', options=None):
    """
    Create specified model
    """
    class Meta:
        # Using type('Meta', ...) gives a dictproxy error during model creation
        pass

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)

    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.iteritems():
            setattr(Meta, key, value)

    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': module, 'Meta': Meta}

    # Add in any fields that were provided
    if fields:
        attrs.update(fields)

    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (models.Model,), attrs)

    return model


def SlugTraits(base_filed_name='name', slug_field_name='slug'):
    """
    Функция генерирующая Mixin к модели
    Добавляющий _slug поле к указанному полю
    При сохраении в это поле записывается slug от указанного поля
    Описание класса на метаязыке
    class SlugMixin(models.Model):
        base_filed_name + '_slug' = models.CharField(verbose_name=_(u'Название для url'),
                                                     max_length=150, blank=True, null=True)
        class Meta:
            abstract = True
    """
    fields = {
        slug_field_name: models.SlugField(verbose_name=u'slug', max_length=150, blank=True, null=True)
    }
    SlugMixin = create_model('SlugMixin', fields=fields, module='main.models', options={'abstract': True})

    def save(self, **kwargs):
        """
        Перегружаем оператор save
        При сохранении записываем slug от указанного поля в новое поле
        """
        original_text = getattr(self, base_filed_name)
        slug_text = pytils.translit.slugify(original_text)
        setattr(self, slug_field_name, slug_text)
        return super(SlugMixin, self).save(**kwargs)
    setattr(SlugMixin, 'save', save)
    return SlugMixin
