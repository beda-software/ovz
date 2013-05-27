# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class ProfessionAbility(models.Model):
    ability = models.CharField(max_length=200, verbose_name=u"Способность")


class ProfessionContraindications(models.Model):
    contraindication = models.CharField(max_length=200, verbose_name=u"Противопоказание")


class Profession(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название")
    characteristic = models.TextField(verbose_name=u"Общая характеристика")
    content = models.TextField(verbose_name=u"Содержание труда")
    ability = models.ManyToManyField('ProfessionAbility', verbose_name=u"Требования к способностям специалиста")
    contraindications = models.ManyToManyField('ProfessionContraindications', verbose_name=u"Противопоказания")