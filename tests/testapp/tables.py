from reinhardt.tables.tables import ReinhardtTable
from reinhardt.tests.testapp.models import TestModel


class TestTable(ReinhardtTable):

    class Meta:
        model = TestModel
        template_name = "apply/tables/table.html"
        fields = ("test_field", )
