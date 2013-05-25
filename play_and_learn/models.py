# -*- coding: utf-8 -*
from django.db import models
from pytils.translit import slugify


class ProfessionsLetter(models.Model):
    letter = models.CharField(max_length=1, verbose_name=u'Символ')
    letter_slug = models.SlugField(verbose_name=u'Слуг символа', blank=True, null=True)

    @models.permalink
    def get_profession_list_url(self):
        return ('play_and_learn.profession_list', (), {'slug':self.letter_slug })

    def get_image_name(self):
        return 'letter_{0}.png'.format(self.letter_slug)

    def __unicode__(self):
        return self.letter

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.letter_slug = slugify(self.letter)
        super(ProfessionsLetter, self).save(force_insert=force_insert, force_update=force_update,
                                            using=using, update_fields=update_fields)


class ProfessionsABC(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    description = models.TextField(verbose_name=u'Описание')
    first_letter = models.ForeignKey('play_and_learn.ProfessionsLetter',
                                     verbose_name=u'Первый символ', blank=True, null=True)

    class Meta:
        verbose_name = u'Профессия'
        verbose_name_plural = u'Профессии'

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.first_letter, created = ProfessionsLetter.objects.get_or_create(letter=self.name[0].lower())
        super(ProfessionsABC, self).save(force_insert=force_insert, force_update=force_update,
                                         using=using, update_fields=update_fields)