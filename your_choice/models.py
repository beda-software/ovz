# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from pytils.translit import slugify


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


class Profession(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название")
    characteristic = models.TextField(verbose_name=u"Общая характеристика")
    content = models.TextField(verbose_name=u"Содержание труда")
    ability = models.ManyToManyField('ProfessionAbility',
                                     verbose_name=u"Требования к способностям специалиста", blank=True, null=True)
    contraindications = models.ManyToManyField('ProfessionContraindications',
                                               verbose_name=u"Противопоказания", blank=True, null=True)
    image = models.ImageField(upload_to='profession_image/')
    slug = models.SlugField(verbose_name=u'Slug')

    @models.permalink
    def get_absolute_url(self):
        return ('your_choice.detail', (), {'slug':self.slug })

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(Profession, self).save(force_insert=force_insert, force_update=force_update,
                                     using=using, update_fields=update_fields)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Профессия'
        verbose_name_plural = u'Профессии'