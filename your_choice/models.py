# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from main.mixins import SlugTraits


class ProfessionAbility(models.Model):
    ability = models.CharField(max_length=200, verbose_name=u"Способность")

    def __unicode__(self):
        return self.ability

    class Meta:
        verbose_name = u'Способность'
        verbose_name_plural = u'Cпособности специалиста'


class ProfessionContraindications(models.Model):
    contraindication = models.CharField(max_length=200, verbose_name=u"Противопоказание")

    def __unicode__(self):
        return self.contraindication

    class Meta:
        verbose_name = u'Противопоказание'
        verbose_name_plural = u'Противопоказания'


class Profession(SlugTraits(), models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название", unique=True)
    characteristic = RichTextField(verbose_name=u"Общая характеристика")
    content = RichTextField(verbose_name=u"Содержание труда")
    ability = models.ManyToManyField('ProfessionAbility',
                                     verbose_name=u"Требования к способностям специалиста", blank=True, null=True)
    contraindications = models.ManyToManyField('ProfessionContraindications',
                                               verbose_name=u"Противопоказания", blank=True, null=True)
    image = models.ImageField(upload_to='profession_image/')

    @models.permalink
    def get_absolute_url(self):
        return ('your_choice.detail', (), {'slug': self.slug})

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Профессия'
        verbose_name_plural = u'Профессии'