# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models
from pytils.translit import slugify


class School(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название")
    contacts = models.CharField(max_length=300, verbose_name=u"Контакты")
    establishing = RichTextField(verbose_name=u"Об учереждении")
    specialties = RichTextField(verbose_name=u"О специальностях", blank=True, null=True)
    rules = RichTextField(verbose_name=u"Правила приема", blank=True, null=True)
    advanced = RichTextField(verbose_name=u"Дополнительная информация", blank=True, null=True)
    image = models.ImageField(upload_to='schools_image/')
    professions = models.ManyToManyField('your_choice.Profession', verbose_name=u'Профессии')
    slug = models.SlugField(verbose_name=u'Slug')

    @models.permalink
    def get_absolute_url(self):
        return ('schools.detail', (), {'slug':self.slug })

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(School, self).save(force_insert=force_insert, force_update=force_update,
                                 using=using, update_fields=update_fields)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Учебное заведение'
        verbose_name_plural = u'Учебные заведения'