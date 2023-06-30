import base64
import hashlib

from django import template
from django.conf import settings
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
def index(item_list, item):
    """
    Template tag for returning an item's index in a list

    :param item_list
    :param item
    :returns integer index for the location of the item within the list
    """
    return item_list.index(item)


@register.filter
def get_item(dictionary, key):
    """
    Template tag used in a django template to get a dict key's value

    :param dictionary
    :param key
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
    try:
        site = Site.objects.get(name__icontains=site_name)
        domain = site.domain
    except Site.DoesNotExist:
        domain = site_name
    return f'https://{domain}'


@register.simple_tag
def to_list(*args):
    """
    Template tag used in a django template create a list

    :param args
    :returns args
    """
    return args


@register.simple_tag
def get_validation_key(transaction_id, amount):
    """
    Template tag used to get the validation key to post data to Touchnet.
    Concatenates values into a strin, gets unencoded data bytes, gets the byte
    encoded string, and decodes the string.

    :param transaction_id: Ex. 1234
    :param amount: Can be integer, float, or string. Ex. 50 or 50.00 or "50"
    :return: decoded string
    """
    secret_key = settings.TOUCHNET["SECRET_KEY"]
    m = hashlib.md5()
    m.update(f"{secret_key}{transaction_id}{amount}".encode("utf-8"))
    return base64.b64encode(m.digest()).decode()
