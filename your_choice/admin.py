# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Profession, ProfessionAbility, ProfessionContraindications

__author__ = 'jackdevil'


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_characteristic', 'short_content',
                    'short_contraindications', 'short_ability')
    exclude = ('slug',)
    truncate_char = 30

    def short_ability(self, obj):
        text = ', '.join(item.ability for item in obj.ability.all())
        if len(text) > self.truncate_char:
            return u'{0}...'.format(text[0:self.truncate_char-3])
        else:
            return text

    def short_contraindications(self, obj):
        text = ', '.join(item.contraindication for item in obj.contraindications.all())
        if len(text) > self.truncate_char:
            return u'{0}...'.format(text[0:self.truncate_char-3])
        else:
            return text

    def short_characteristic(self, obj):
        if len(obj.characteristic) > self.truncate_char:
            return u'{0}...'.format(obj.characteristic[0:self.truncate_char-3])
        else:
            return obj.characteristic

    def short_content(self, obj):
        if len(obj.content) > self.truncate_char:
            return u'{0}...'.format(obj.content[0:self.truncate_char-3])
        else:
            return obj.content

    short_characteristic.short_description = u'Общая характеристика'
    short_content.short_description = u'Содержание труда'
    short_contraindications.short_description = u'Противопоказания'
    short_ability.short_description = u'Способности специалиста'


class ProfessionAbilityAdmin(admin.ModelAdmin):
    list_display = ('ability',)


class ProfessionContraindicationsAdmin(admin.ModelAdmin):
    list_display = ('contraindication',)

admin.site.register(Profession, ProfessionAdmin)
admin.site.register(ProfessionAbility, ProfessionAbilityAdmin)
admin.site.register(ProfessionContraindications, ProfessionContraindicationsAdmin)
