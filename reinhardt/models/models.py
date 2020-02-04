import rules
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Model, DateTimeField
from django_currentuser.db.models import CurrentUserField

from reinhardt.utils import get_child
from .managers import ObjectManager
from rules.contrib.models import RulesModelBase, RulesModelMixin


class ReinhardtModelBase(RulesModelBase):

    def __new__(cls, name, bases, attrs, **kwargs):
        # Ensure initialization is only performed for subclasses of Model
        # (excluding Model class itself).
        parents = [b for b in bases if isinstance(b, ReinhardtModelBase)]
        if not parents or not getattr(settings, 'REQUIRE_DB_TABLE_NAMES', False):
            return super().__new__(cls, name, bases, attrs, **kwargs)

        model_meta = attrs.get("Meta")
        if not hasattr(model_meta, "db_table"):
            module = attrs.get('__module__')
            raise ImproperlyConfigured("%s.%s does not declare a db_table name." % (module, name))

        return super().__new__(cls, name, bases, attrs, **kwargs)


class AuditModel(RulesModelMixin, Model, metaclass=ReinhardtModelBase):
    """
    .. note:: - Requires **django-currentuser**

    :tags:
        django-currentuser
    """

    last_updated_by = CurrentUserField(related_name='%(app_label)s_%(class)s_last_updated')
    last_updated_at = DateTimeField(auto_now=True)
    created_by = CurrentUserField(related_name='%(app_label)s_%(class)s_last_created')
    created_at = DateTimeField(auto_now_add=True)

    objects = ObjectManager()

    class Meta:
        abstract = True
        rules_permissions = {
            "add": rules.always_true,
            "update": rules.always_true,
            "delete": rules.always_true,
            "view": rules.always_true,
            "view_list": rules.always_true
        }

    @property
    def child(self):
        return get_child(self)
