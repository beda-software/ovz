# -*- coding: utf-8 -*-
from django.views.generic import ListView, TemplateView
from models import Job
from mixins import JobNavigateMixin, TotalInfoNavigateMixin


class TotalInfoList(TotalInfoNavigateMixin, TemplateView):
    template_name = 'labor_market/total_info/list.html'


class JobList(JobNavigateMixin, ListView):
    model = Job
    template_name = 'labor_market/job/list.html'
    paginate_by = 5