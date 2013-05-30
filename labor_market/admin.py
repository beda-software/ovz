__author__ = 'jackdevil'
from django.contrib import admin
from models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'contacts', 'create', 'edit')
    truncate_char = 30

    def short_description(self, obj):
        if len(obj.description) > self.truncate_char:
            return u'{0}...'.format(obj.description[0:self.truncate_char-3])
        else:
            return obj.description

admin.site.register(Job, JobAdmin)
