# -*- coding: utf-8 -*-
from django.db import models
from django.core.mail import send_mail

from ovz.settings import EMAIL_NOTICE_GUEST, EMAIL_HOST_USER

# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Ваше имя *')
    email = models.EmailField(verbose_name=u'Ваш E-mail', blank=True, null=True)
    message = models.TextField(verbose_name=u'Сообщение *')
    notice = models.BooleanField(default=False, verbose_name=u'Уведомить об ответе на E-mail')
    answer = models.TextField(verbose_name=u'Ответ администратора', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name=u'Создано')
    edit = models.DateTimeField(auto_now=True, verbose_name=u'Изменено')

    def __unicode__(self):
        return u'Сообщение от {0}'.format(self.name)

    class Meta:
        verbose_name = u'Сообщение'
        verbose_name_plural = u'Гостевая книга'

    def save(self, force_insert=False, force_update=False, using=None):
        super(Guest, self).save()
        title = u'В гостевую книгу добавлена новая запись!'

        content = u'В гостевую книгу добавлена новая запись!\n\n'
        content+= u'Отправитель: ' + self.name + '\n' + u'Сообщение: ' + self.message + '\n'

        send_mail(title, content, EMAIL_HOST_USER, [EMAIL_NOTICE_GUEST])

