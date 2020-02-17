from django_tables2 import tables, TemplateColumn


class ActionColumnMixin(tables.Table):
    actions = TemplateColumn(template_name='apply/tables/actions.html', orderable=False)
