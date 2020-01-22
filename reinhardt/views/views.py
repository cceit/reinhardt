from django.views.generic import CreateView
from django_tables2 import SingleTableView
from rules.contrib.views import PermissionRequiredMixin


class ReinhardtListView(PermissionRequiredMixin, SingleTableView):
    template_name = 'apply/list.html'
    permission_required = 'read'


class ReinhardtCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'apply/form.html'
    permission_required = 'add'
