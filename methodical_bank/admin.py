# -*- coding: utf-8 -*-
from django.contrib import admin
from models import MethodicalBank

__author__ = 'jackdevil'


class MethodicalBankAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'attached',)
    exclude = ('slug',)

admin.site.register(MethodicalBank, MethodicalBankAdmin)
