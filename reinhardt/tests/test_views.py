import unittest

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.test import RequestFactory, TestCase

from reinhardt.tests.testapp.models import TestModel, TestRestrictedModel, TestStaffOnlyModel
from reinhardt.tests.testapp.views import TestCreateView, TestListView, TestRestrictedListView, TestStaffOnlyListView, \
    TestRestrictedCreateView, TestStaffOnlyCreateView


class TestViewPermissions(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.staff_user = User.objects.create_user(username='John', email='john@test.com', password='top_secret')
        self.staff_user.is_staff = True
        self.staff_user.save()
        self.test_model_instance = TestModel.objects.create(test_field='test')
        self.test_restricted_model_instance = TestRestrictedModel.objects.create(test_field='test')
        self.test_staff_only_model_instance = TestStaffOnlyModel.objects.create(test_field='test')

    def test_list_view_permissions(self):
        self.view_permission_tester(TestListView, self.user, True)
        self.view_permission_tester(TestListView, self.staff_user, True)
        self.view_permission_tester(TestRestrictedListView, self.user, False)
        self.view_permission_tester(TestRestrictedListView, self.staff_user, False)
        self.view_permission_tester(TestStaffOnlyListView, self.user, False)
        self.view_permission_tester(TestStaffOnlyListView, self.staff_user, True)

    def test_create_view_permissions(self):
        self.view_permission_tester(TestCreateView, self.user, True)
        self.view_permission_tester(TestCreateView, self.staff_user, True)
        self.view_permission_tester(TestRestrictedCreateView, self.user, False)
        self.view_permission_tester(TestRestrictedCreateView, self.staff_user, False)
        self.view_permission_tester(TestStaffOnlyCreateView, self.user, False)
        self.view_permission_tester(TestStaffOnlyCreateView, self.staff_user, True)

    def view_permission_tester(self, view_class, user, permitted):
        request = RequestFactory().get('/')
        request.user = user
        if permitted:
            response = view_class.as_view()(request)
            assert response.status_code == 200
        else:
            try:
                view_class.as_view()(request)
                assert False, "Expected to get permission denied, but did not."
            except PermissionDenied:
                pass


if __name__ == '__main__':
    unittest.main()
