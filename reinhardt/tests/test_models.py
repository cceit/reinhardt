from django.test import TestCase

from reinhardt.tests.testapp.models import TestModel


class TestModels(TestCase):
    def setUp(self):
        self.model_instance = TestModel.objects.create(test_field='test text')

    def test_get_or_none(self):
        assert TestModel.objects.get_or_none(pk=self.model_instance.pk)
        assert not TestModel.objects.get_or_none(pk=32)
