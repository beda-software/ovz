# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Profession, ProfessionAbility, ProfessionContraindications

__author__ = 'jackdevil'


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('slug',)


class ProfessionAbilityAdmin(admin.ModelAdmin):
    list_display = ('ability',)


class ProfessionContraindicationsAdmin(admin.ModelAdmin):
    list_display = ('contraindication',)

admin.site.register(Profession, ProfessionAdmin)
admin.site.register(ProfessionAbility, ProfessionAbilityAdmin)
admin.site.register(ProfessionContraindications, ProfessionContraindicationsAdmin)
