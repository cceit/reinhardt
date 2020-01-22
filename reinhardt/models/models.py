from django.db.models import Model, DateTimeField
from django_currentuser.db.models import CurrentUserField

from reinhardt.utils import get_child
from .managers import ObjectManager
from rules.contrib.models import RulesModelBase, RulesModelMixin


class AuditModel(RulesModelMixin, Model, metaclass=RulesModelBase):
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

    @property
    def child(self):
        return get_child(self)