from django.urls import path
from reinhardt.tests.testapp.views import TestListView, TestRestrictedListView, TestStaffOnlyListView, TestCreateView, \
    TestRestrictedCreateView, TestStaffOnlyCreateView, TestRestrictedUpdateView, TestStaffOnlyUpdateView, TestUpdateView

urlpatterns = [
    path('list/', TestListView.as_view(), name='list-view'),
    path('restricted-list/', TestRestrictedListView.as_view(), name='restricted-list-view'),
    path('staff-only-list/', TestStaffOnlyListView.as_view(), name='staff-only-list-view'),
    path('create/', TestCreateView.as_view(), name='create-view'),
    path('restricted-create/', TestRestrictedCreateView.as_view(), name='restricted-create-view'),
    path('staff-only-create/', TestStaffOnlyCreateView.as_view(), name='staff-only-create-view'),
    path('update/<int:pk>/', TestUpdateView.as_view(), name='update-view'),
    path('restricted-update/<int:pk>/', TestRestrictedUpdateView.as_view(), name='restricted-update-view'),
    path('staff-only-update/<int:pk>/', TestStaffOnlyUpdateView.as_view(), name='staff-only-update-view'),
]
