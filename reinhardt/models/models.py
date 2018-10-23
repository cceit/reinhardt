from cuser.fields import CurrentUserField
from django.db.models import Model, DateTimeField

from reinhardt.utils import get_child
from .managers import ObjectManager
from .mixins import ModelPermissionsMixin


class AuditModel(ModelPermissionsMixin, Model):
    """
    .. note:: - Requires **django-cuser**

    :tags:
        django-cuser
    """

    last_updated_by = CurrentUserField(related_name='%(app_label)s_%(class)s_last_updated')
    last_updated_at = DateTimeField(auto_now=True)
    created_by = CurrentUserField(add_only=True, related_name='%(app_label)s_%(class)s_last_created')
    created_at = DateTimeField(auto_now_add=True)

    objects = ObjectManager()

    class Meta:
        abstract = True

    @property
    def child(self):
        return get_child(self)