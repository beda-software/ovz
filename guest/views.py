# -*- coding: utf-8 -*-
# Create your views here.
from django.core.urlresolvers import reverse
from django.http import Http404

from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from guest.forms import GuestForm
from guest.mixins import GuestNavigateMixin
from guest.models import Guest


class GuestView(GuestNavigateMixin, FormMixin,  ListView):
    form_class = GuestForm
    model = Guest
    paginate_by = 5
    template_name = 'guest/guest.html'

    def get_success_url(self):
        return reverse('guest')

    def get_queryset(self):
        return self.model.objects.exclude(answer__isnull=True).exclude(answer__exact='')

    def get_context_data(self, **kwargs):
        context = super(GuestView, self).get_context_data(**kwargs)
        context['count'] = len(self.get_queryset())
        return context

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            raise Http404(u"Empty list and '%(class_name)s.allow_empty' is False."
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.object_list = self.get_queryset()
        if self.form.is_valid():
            return self.form_valid(self.form)
        else:
            return self.form_invalid(self.form)

    def form_valid(self, form):
        form.save()
        return super(GuestView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(object_list=self.object_list, form=self.form)
        )