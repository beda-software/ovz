# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from pytils.translit import slugify


class MethodicalBank(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название')
    description = models.TextField(verbose_name=u'Описание')
    author = models.CharField(max_length=100, verbose_name=u'Автор')
    attached = models.FileField(upload_to='metodical_bank/', verbose_name=u'Файл')
    create = models.DateTimeField(auto_now_add=True, verbose_name=u'Создано')
    edit = models.DateTimeField(auto_now=True, verbose_name=u'Изменено')
    slug = models.SlugField(verbose_name=u'Slug')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(MethodicalBank, self).save(force_insert=force_insert, force_update=force_update,
                                         using=using, update_fields=update_fields)

    @models.permalink
    def get_absolute_url(self):
        return ('metodical_bank.detail', (), {'slug':self.slug })

    def __unicode__(self):
        return u'{0} от {1}'.format(self.name, self.author)

    class Meta:
        verbose_name = u'Материал'
        verbose_name_plural = u'Методическая копилка'