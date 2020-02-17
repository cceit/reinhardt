from collections import OrderedDict

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django_tables2 import SingleTableView
from reinhardt.views.mixins import ViewMetaMixin, DeleteMetaMixin
from rules.contrib.views import AutoPermissionRequiredMixin


class ReinhardtView(AutoPermissionRequiredMixin):
    permission_type_map = [
        (CreateView, "add"),
        (UpdateView, "update"),
        (DeleteView, "delete"),
        (DetailView, "view"),
        (SingleTableView, "view_list"),
    ]
    page_title = ''

    def get_page_title(self):
        if not self.page_title:
            raise ImproperlyConfigured("page_title is not set")
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super(ReinhardtView, self).get_context_data(**kwargs)
        context.update({
            'page_title': self.get_page_title(),
        })
        return context


class ReinhardtListView(ReinhardtView, SingleTableView):
    template_name = 'apply/list.html'


class ReinhardtCreateView(ReinhardtView, CreateView):
    template_name = 'apply/form.html'


class ReinhardtUpdateView(ReinhardtView, UpdateView):
    template_name = 'apply/form.html'


class ReinhardtDeleteView(DeleteMetaMixin, ReinhardtView, DeleteView):
    template_name = 'apply/delete.html'


class ReinhardtDetailView(ViewMetaMixin, ReinhardtView, DetailView):
    template_name = 'apply/detail.html'
