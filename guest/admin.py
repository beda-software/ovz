# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Guest

__author__ = 'jackdevil'


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'answer', 'create')

admin.site.register(Guest, GuestAdmin)
