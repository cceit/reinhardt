from reinhardt.views import ReinhardtCreateView, ReinhardtListView, ReinhardtUpdateView
from reinhardt.tests.testapp.models import TestModel, TestRestrictedModel, TestStaffOnlyModel


class TestListView(ReinhardtListView):
    model = TestModel


class TestRestrictedListView(ReinhardtListView):
    model = TestRestrictedModel


class TestStaffOnlyListView(ReinhardtListView):
    model = TestStaffOnlyModel


class TestCreateView(ReinhardtCreateView):
    model = TestModel
    fields = ('test_field', )


class TestRestrictedCreateView(ReinhardtCreateView):
    model = TestRestrictedModel
    fields = ('test_field',)


class TestStaffOnlyCreateView(ReinhardtCreateView):
    model = TestStaffOnlyModel
    fields = ('test_field',)


class TestUpdateView(ReinhardtUpdateView):
    model = TestModel
    fields = ('test_field', )


class TestRestrictedUpdateView(ReinhardtUpdateView):
    model = TestRestrictedModel
    fields = ('test_field',)


class TestStaffOnlyUpdateView(ReinhardtUpdateView):
    model = TestStaffOnlyModel
    fields = ('test_field',)
