from django import template
from django.contrib.sites.models import Site
from django.forms import widgets

register = template.Library()

@register.filter
def is_date_field(formfield):
    """
    Template tag used in a django template to check if a form field is a
     date field

    :param FormField formfield: Django form field
    :returns bool: True if FormField is a date field
    """
    styled_widgets = [widgets.DateInput,
                      ]
    return type(formfield.field.widget) in styled_widgets


@register.filter
def is_datetime_field(formfield):
    """
    Template tag used in a django template to check if a form field is a
     datetime field

    :param FormField formfield: Django form field
    :returns bool: True if FormField is a datetime field
    """
    styled_widgets = [widgets.DateTimeInput,
                      ]
    return type(formfield.field.widget) in styled_widgets

@register.filter
def groups(user):
    """
    Template tag used in a django template to check a user's groups

    :param user
    :returns list of names of groups that a user belongs to
    """
    return [group.name for group in user.groups.all()]


@register.filter
def index(list, choice):
    """
    Template tag used in a django template to check a user's groups

    :param list, choice
    :returns list of names of groups that a user belongs to
    """
    return list.index(choice)


@register.filter
def get_item(dictionary, key):
    """
    Template tag used in a django template to get a dict key's value

    :param dictionary, key
    :returns None or key's value in dict
    """
    return dictionary.get(key, None)


@register.filter
def get_domain(site_name):
    """
    Template tag used in a django template to get a site's domain based off of it's name

    :param site_name
    :returns domain
    """
    return f'https://{Site.objects.get(name__icontains=site_name).domain}'


@register.simple_tag
def to_list(*args):
    """
    Template tag used in a django template to get a dict key's value

    :param dictionary, key
    :returns None or key's value in dict
    """
    return args
