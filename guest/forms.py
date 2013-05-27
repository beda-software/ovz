# -*- coding: utf-8 -*-
from django import forms
from models import Guest

__author__ = 'jackdevil'


class GuestForm(forms.ModelForm):
    def clean(self):
        super(GuestForm, self).clean()
        cleaned_data = self.cleaned_data
        if not 'notice' in cleaned_data or not 'email' in cleaned_data:
            return cleaned_data
        if cleaned_data['notice'] and not cleaned_data['email']:
            self._errors['email'] = [u'Укажите email для уведомлений.']
        return cleaned_data

    class Meta:
        model = Guest
        exclude = ['answer']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': u'Ваше имя *'}),
            'email': forms.TextInput(attrs={'placeholder': u'Ваш E-mail'}),
            'message': forms.Textarea(attrs={'placeholder': u'Сообщение *'}),
        }