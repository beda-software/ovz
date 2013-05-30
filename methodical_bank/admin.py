# -*- coding: utf-8 -*-
from django.contrib import admin
from models import MethodicalBank

__author__ = 'jackdevil'


class MethodicalBankAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'short_about_author',
                    'short_methodology', 'attached',)
    exclude = ('slug',)

    def short_about_author(self, obj):
        if len(obj.about_author) > self.truncate_char:
            return u'{0}...'.format(obj.about_author[0:self.truncate_char-3])
        else:
            return obj.about_author

    def short_methodology(self, obj):
        if len(obj.methodology) > self.truncate_char:
            return u'{0}...'.format(obj.methodology[0:self.truncate_char-3])
        else:
            return obj.methodology

    short_about_author.short_description = u'О авторе'
    short_methodology.short_description = u'О методике'

admin.site.register(MethodicalBank, MethodicalBankAdmin)
