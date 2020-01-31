from django.urls import reverse

from reinhardt.views import ReinhardtCreateView, ReinhardtListView, ReinhardtUpdateView, ReinhardtDetailView, \
    ReinhardtDeleteView
from reinhardt.tests.testapp.models import TestModel, TestRestrictedModel, TestStaffOnlyModel


# List Views
class TestListView(ReinhardtListView):
    model = TestModel
    page_title = 'List'


class TestRestrictedListView(ReinhardtListView):
    model = TestRestrictedModel
    page_title = 'Restricted List'


class TestStaffOnlyListView(ReinhardtListView):
    model = TestStaffOnlyModel
    page_title = 'Staff Only List'


# Create Views
class TestCreateView(ReinhardtCreateView):
    model = TestModel
    fields = ('test_field', )
    page_title = 'Create'


class TestRestrictedCreateView(ReinhardtCreateView):
    model = TestRestrictedModel
    fields = ('test_field',)
    page_title = 'Restricted Create'


class TestStaffOnlyCreateView(ReinhardtCreateView):
    model = TestStaffOnlyModel
    fields = ('test_field',)
    page_title = 'Staff Only Create'


# Update Views
class TestUpdateView(ReinhardtUpdateView):
    model = TestModel
    fields = ('test_field', )
    page_title = 'Update'


class TestRestrictedUpdateView(ReinhardtUpdateView):
    model = TestRestrictedModel
    fields = ('test_field',)
    page_title = 'Restricted Update'


class TestStaffOnlyUpdateView(ReinhardtUpdateView):
    model = TestStaffOnlyModel
    fields = ('test_field',)
    page_title = 'Staff Only Update'


class TestDetailView(ReinhardtDetailView):
    model = TestModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )
    page_title = 'Detail'


class TestRestrictedDetailView(ReinhardtDetailView):
    model = TestRestrictedModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )
    page_title = 'Restricted Detail'


class TestStaffOnlyDetailView(ReinhardtDetailView):
    model = TestStaffOnlyModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )
    page_title = 'Staff Only Detail'


class TestDeleteView(ReinhardtDeleteView):
    model = TestModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )
    page_title = 'Delete'

    def get_success_url(self):
        return reverse('list-view')


class TestRestrictedDeleteView(ReinhardtDeleteView):
    model = TestRestrictedModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )
    page_title = 'Restricted Delete'

    def get_success_url(self):
        return reverse('list-view')


class TestStaffOnlyDeleteView(ReinhardtDeleteView):
    model = TestStaffOnlyModel
    detail_fields = (
        ('Test Field', 'test_field'),
    )
    page_title = 'Staff Only Delete'

    def get_success_url(self):
        return reverse('list-view')
