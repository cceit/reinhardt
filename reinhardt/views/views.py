from django.core.exceptions import ImproperlyConfigured
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django_tables2 import SingleTableView
from rules.contrib.views import AutoPermissionRequiredMixin


class ReinhardtView(AutoPermissionRequiredMixin):
    permission_type_map = [
        (CreateView, "add"),
        (UpdateView, "change"),
        (DeleteView, "delete"),
        (DetailView, "view"),
        (SingleTableView, "view_list"),
    ]

    def get_permission_required(self):
        """Adds the correct permission to check according to view type."""
        try:
            perm_type = self.permission_type
        except AttributeError:
            # Perform auto-detection by view type
            for view_type, _perm_type in self.permission_type_map:
                if isinstance(self, view_type) or issubclass(self.__class__, view_type):
                    perm_type = _perm_type
                    break
            else:
                raise ImproperlyConfigured(
                    "AutoPermissionRequiredMixin was used, but permission_type was "
                    "neither set nor could be determined automatically for {0}. "
                    "Consider setting permission_type on the view manually or "
                    "adding {0} to the permission_type_map."
                    .format(self.__class__.__name__)
                )

        perms = []
        if perm_type is not None:
            model = getattr(self, "model", None)
            if model is None:
                model = self.get_queryset().model
            perms.append(model.get_perm(perm_type))

        # If additional permissions have been defined, consider them as well
        if self.permission_required is not None:
            perms.extend(super().get_permission_required())
        return perms


class ReinhardtListView(ReinhardtView, SingleTableView):
    template_name = 'apply/list.html'


class ReinhardtCreateView(ReinhardtView, CreateView):
    template_name = 'apply/form.html'
