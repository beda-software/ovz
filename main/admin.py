from django.forms.models import modelform_factory
from django.contrib import admin
from flatblocks.admin import FlatBlockAdmin
from flatblocks.models import FlatBlock
from ckeditor.fields import CKEditorWidget

class NewFlatBlockAdmin(FlatBlockAdmin):
    form = modelform_factory(FlatBlock,widgets={'content': CKEditorWidget})

admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, NewFlatBlockAdmin)

