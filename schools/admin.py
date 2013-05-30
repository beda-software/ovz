# -*- coding: utf-8 -*-
from django.contrib import admin
from models import School

__author__ = 'jackdevil'


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_contacts', 'short_establishing',
                    'short_specialties', 'short_rules', 'short_advanced', 'short_professions')
    exclude = ('slug',)
    truncate_char = 30

    def short_professions(self, obj):
        text = ', '.join(item.name for item in obj.professions.all())
        if len(text) > self.truncate_char:
            return u'{0}...'.format(text[0:self.truncate_char-3])
        else:
            return text

    def short_contacts(self, obj):
        if len(obj.contacts) > self.truncate_char:
            return u'{0}...'.format(obj.contacts[0:self.truncate_char-3])
        else:
            return obj.contacts

    def short_establishing(self, obj):
        if len(obj.establishing) > self.truncate_char:
            return u'{0}...'.format(obj.establishing[0:self.truncate_char-3])
        else:
            return obj.establishing

    def short_specialties(self, obj):
        if len(obj.specialties) > self.truncate_char:
            return u'{0}...'.format(obj.specialties[0:self.truncate_char-3])
        else:
            return obj.specialties

    def short_rules(self, obj):
        if len(obj.rules) > self.truncate_char:
            return u'{0}...'.format(obj.rules[0:self.truncate_char-3])
        else:
            return obj.rules

    def short_advanced(self, obj):
        if len(obj.advanced) > self.truncate_char:
            return u'{0}...'.format(obj.advanced[0:self.truncate_char-3])
        else:
            return obj.advanced

    short_professions.short_description = u'Профессии'
    short_contacts.short_description = u'Контакты'
    short_establishing.short_description = u'Об учереждении'
    short_specialties.short_description = u'О специальностях'
    short_rules.short_description = u'Правила приема'
    short_advanced.short_description = u'Дополнительная информация'

admin.site.register(School, SchoolAdmin)
