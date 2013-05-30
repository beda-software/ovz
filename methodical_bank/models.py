# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models
from main.mixins import SlugTraits


class MethodicalBank(SlugTraits(), models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название', unique=True)
    author = models.CharField(max_length=100, verbose_name=u'Автор')
    about_author = RichTextField(verbose_name=u'Об авторе')
    methodology = RichTextField(verbose_name=u'О методике')
    attached = models.FileField(upload_to='metodical_bank/', verbose_name=u'Файл')
    create = models.DateTimeField(auto_now_add=True, verbose_name=u'Создано')
    edit = models.DateTimeField(auto_now=True, verbose_name=u'Изменено')

    @models.permalink
    def get_absolute_url(self):
        return ('metodical_bank.detail', (), {'slug':self.slug })

    def __unicode__(self):
        return u'{0} от {1}'.format(self.name, self.author)

    class Meta:
        verbose_name = u'Материал'
        verbose_name_plural = u'Методическая копилка'