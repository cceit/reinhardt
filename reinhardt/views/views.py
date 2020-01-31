from collections import OrderedDict

from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django_tables2 import SingleTableView
from reinhardt.views.mixins import ViewMetaMixin
from rules.contrib.views import AutoPermissionRequiredMixin


class ReinhardtView(AutoPermissionRequiredMixin):
    permission_type_map = [
        (CreateView, "add"),
        (UpdateView, "change"),
        (DeleteView, "delete"),
        (DetailView, "view"),
        (SingleTableView, "view_list"),
    ]


class ReinhardtListView(ReinhardtView, SingleTableView):
    template_name = 'apply/list.html'


class ReinhardtCreateView(ReinhardtView, CreateView):
    template_name = 'apply/form.html'


class ReinhardtUpdateView(ReinhardtView, UpdateView):
    template_name = 'apply/form.html'


class ReinhardtDetailView(ViewMetaMixin, ReinhardtView, DetailView):
    template_name = 'apply/detail.html'

