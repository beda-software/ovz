__author__ = 'jackdevil'
from django.contrib import admin
from models import ProfessionsABC


class ProfessionsABCAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'first_letter')
    exclude = ('first_letter',)

admin.site.register(ProfessionsABC, ProfessionsABCAdmin)
