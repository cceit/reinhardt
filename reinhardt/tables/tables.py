from django_tables2 import tables
from reinhardt.tables.mixins import ActionColumnMixin


class ReinhardtTable(ActionColumnMixin, tables.Table):
    pass
