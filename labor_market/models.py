# -*- coding: utf-8 -*
from ckeditor.fields import RichTextField
from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Название")
    description = RichTextField(verbose_name=u"Описание")
    contacts = models.CharField(max_length=100, verbose_name=u"Контакты")
    create = models.DateTimeField(auto_now_add=True, verbose_name=u"Создано")
    edit = models.DateTimeField(auto_now=True, verbose_name=u"Изменено")

    class Meta:
        verbose_name = u'Работа'
        verbose_name_plural = u'Вакансии'

    def __unicode__(self):
        return self.title

