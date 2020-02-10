import rules
from django.db import models
from django.urls import reverse

from reinhardt.models import AuditModel


class TestModel(AuditModel):
    test_field = models.CharField(max_length=30)

    class Meta:
        rules_permissions = {
            'add': rules.always_true,
            'update': rules.always_true,
            'delete': rules.always_true,
            'view': rules.always_true,
            'view_list': rules.always_true
        }

    def get_absolute_url(self):
        return reverse('view_test_model', kwargs={'pk': self.pk})


class TestRestrictedModel(AuditModel):
    test_field = models.CharField(max_length=30)

    class Meta:
        rules_permissions = {
            'add': rules.always_false,
            'update': rules.always_false,
            'delete': rules.always_false,
            'view': rules.always_false,
            'view_list': rules.always_false
        }


class TestStaffOnlyModel(AuditModel):
    test_field = models.CharField(max_length=30)

    class Meta:
        rules_permissions = {
            'add': rules.is_staff,
            'update': rules.is_staff,
            'delete': rules.is_staff,
            'view': rules.is_staff,
            'view_list': rules.is_staff
        }
