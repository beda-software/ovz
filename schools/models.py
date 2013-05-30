# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models
from main.mixins import SlugTraits


class School(SlugTraits(), models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название", unique=True)
    contacts = models.CharField(max_length=300, verbose_name=u"Контакты")
    establishing = RichTextField(verbose_name=u"Об учереждении")
    specialties = RichTextField(verbose_name=u"О специальностях", blank=True, null=True)
    rules = RichTextField(verbose_name=u"Правила приема", blank=True, null=True)
    advanced = RichTextField(verbose_name=u"Дополнительная информация", blank=True, null=True)
    image = models.ImageField(upload_to='schools_image/')
    professions = models.ManyToManyField('your_choice.Profession', verbose_name=u'Профессии')

    @models.permalink
    def get_absolute_url(self):
        return ('schools.detail', (), {'slug':self.slug })

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Учебное заведение'
        verbose_name_plural = u'Учебные заведения'