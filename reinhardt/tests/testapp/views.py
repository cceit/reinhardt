from django.urls import reverse

from reinhardt.views import ReinhardtCreateView, ReinhardtListView, ReinhardtUpdateView, ReinhardtDetailView, \
    ReinhardtDeleteView
from reinhardt.tests.testapp.models import TestModel, TestRestrictedModel, TestStaffOnlyModel


# List Views
class TestListView(ReinhardtListView):
    model = TestModel


class TestRestrictedListView(ReinhardtListView):
    model = TestRestrictedModel


class TestStaffOnlyListView(ReinhardtListView):
    model = TestStaffOnlyModel


# Create Views
class TestCreateView(ReinhardtCreateView):
    model = TestModel
    fields = ('test_field', )


class TestRestrictedCreateView(ReinhardtCreateView):
    model = TestRestrictedModel
    fields = ('test_field',)


class TestStaffOnlyCreateView(ReinhardtCreateView):
    model = TestStaffOnlyModel
    fields = ('test_field',)


# Update Views
class TestUpdateView(ReinhardtUpdateView):
    model = TestModel
    fields = ('test_field', )


class TestRestrictedUpdateView(ReinhardtUpdateView):
    model = TestRestrictedModel
    fields = ('test_field',)


class TestStaffOnlyUpdateView(ReinhardtUpdateView):
    model = TestStaffOnlyModel
    fields = ('test_field',)


class TestDetailView(ReinhardtDetailView):
    model = TestModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )


class TestRestrictedDetailView(ReinhardtDetailView):
    model = TestRestrictedModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )


class TestStaffOnlyDetailView(ReinhardtDetailView):
    model = TestStaffOnlyModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )


class TestDeleteView(ReinhardtDeleteView):
    model = TestModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )

    def get_success_url(self):
        return reverse('list-view')


class TestRestrictedDeleteView(ReinhardtDeleteView):
    model = TestRestrictedModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )

    def get_success_url(self):
        return reverse('list-view')


class TestStaffOnlyDeleteView(ReinhardtDeleteView):
    model = TestStaffOnlyModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )

    def get_success_url(self):
        return reverse('list-view')
