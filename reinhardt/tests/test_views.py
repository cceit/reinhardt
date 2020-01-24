import unittest

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from reinhardt.tests.testapp.models import TestModel, TestRestrictedModel, TestStaffOnlyModel


class TestViewPermissions(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.staff_user = User.objects.create_user(username='John', email='john@test.com', password='top_secret')
        self.staff_user.is_staff = True
        self.staff_user.save()
        self.test_model_instance = TestModel.objects.create(test_field='test')
        self.test_restricted_model_instance = TestRestrictedModel.objects.create(test_field='test')
        self.test_staff_only_model_instance = TestStaffOnlyModel.objects.create(test_field='test')

    def test_list_view_permissions(self):
        self.view_permission_tester(reverse('list-view'), self.user, True)
        self.view_permission_tester(reverse('list-view'), self.staff_user, True)
        self.view_permission_tester(reverse('restricted-list-view'), self.user, False)
        self.view_permission_tester(reverse('restricted-list-view'), self.staff_user, False)
        self.view_permission_tester(reverse('staff-only-list-view'), self.user, False)
        self.view_permission_tester(reverse('staff-only-list-view'), self.staff_user, True)

    def test_create_view_permissions(self):
        self.view_permission_tester(reverse('create-view'), self.user, True)
        self.view_permission_tester(reverse('create-view'), self.staff_user, True)
        self.view_permission_tester(reverse('restricted-create-view'), self.user, False)
        self.view_permission_tester(reverse('restricted-create-view'), self.staff_user, False)
        self.view_permission_tester(reverse('staff-only-create-view'), self.user, False)
        self.view_permission_tester(reverse('staff-only-create-view'), self.staff_user, True)

    def test_update_view_permissions(self):
        test_pk = self.test_model_instance.pk
        test_restricted_pk = self.test_restricted_model_instance.pk
        test_staff_only_pk = self.test_staff_only_model_instance.pk
        self.view_permission_tester(reverse('update-view', kwargs={'pk': test_pk}), self.user, True)
        self.view_permission_tester(reverse('update-view', kwargs={'pk': test_pk}), self.staff_user, True)
        self.view_permission_tester(reverse('restricted-update-view', kwargs={'pk': test_restricted_pk}), self.user, False)
        self.view_permission_tester(reverse('restricted-update-view', kwargs={'pk': test_restricted_pk}), self.staff_user, False)
        self.view_permission_tester(reverse('staff-only-update-view', kwargs={'pk': test_staff_only_pk}), self.user, False)
        self.view_permission_tester(reverse('staff-only-update-view', kwargs={'pk': test_staff_only_pk}), self.staff_user, True)

    def view_permission_tester(self, url, user, permitted):
        self.client.force_login(user)
        response = self.client.get(url)
        if permitted:
            assert response.status_code == 200, 'Expected to be granted access, but was not'
        else:
            assert response.status_code == 403, 'Expected to be denied access, but was not.'


if __name__ == '__main__':
    unittest.main()
