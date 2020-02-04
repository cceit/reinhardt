from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag
def has_obj_perm(perm, user, obj=None):
    if not hasattr(user, 'has_perm'):  # pragma: no cover
        return False  # swapped user model that doesn't support permissions
    elif not hasattr(obj, 'get_perm'):
        return False  # object does not support reinhardt implementation of rules
    else:
        return user.has_perm(obj.get_perm(perm), obj)

@register.filter
def detail_url(object):
    underscored_model_name = '_'.join(object._meta.verbose_name.lower().split(' '))
    try:
        return reverse(f'view_{underscored_model_name}', kwargs={'pk': object.pk})
    except NoReverseMatch:
        return None

@register.filter
def update_url(object):
    underscored_model_name = '_'.join(object._meta.verbose_name.lower().split(' '))
    try:
        return reverse(f'update_{underscored_model_name}', kwargs={'pk': object.pk})
    except NoReverseMatch:
        return None

@register.filter
def delete_url(object):
    underscored_model_name = '_'.join(object._meta.verbose_name.lower().split(' '))
    try:
        return reverse(f'update_{underscored_model_name}', kwargs={'pk': object.pk})
    except NoReverseMatch:
        return None
