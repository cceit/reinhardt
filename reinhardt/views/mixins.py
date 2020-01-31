from django.core.exceptions import ImproperlyConfigured


class ViewMetaMixin(object):
    """
    Mixin will be used capture optional and required meta data about each view
     that are then passed to the template
    """
    page_title = ''

    def get_page_title(self):
        if not self.page_title:
            raise ImproperlyConfigured("page_title is not set")
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super(ViewMetaMixin, self).get_context_data(**kwargs)
        context.update({
            'page_title': self.get_page_title(),
            'details': self.get_details(),
        })
        return context

    def get_detail_fields(self):
        """
        Override this method to make the details shown dynamic.
        """
        return self.detail_fields

    def get_details(self):
        """
        How self.fields should be formatted:
        - The first item in each tuple should be the label.
        - The second item should be EITHER a dotted path from this object to
        what goes on the page, OR a function that takes exactly one argument.
        - The third item is an optional extra parameter.
        - - If the thing passed is a related manager, this is an optional
        dotted path to apply to each object in the manager.
        Example:
        .. code-block:: python
            :linenos:
            fields = [
                ('Username', 'user.username'),
                ('Passport file', 'passport'),
                ('Zip codes', 'address_set', 'zip_code'),
                ('Active', 'is_active'),
                ('Joined date', 'joined_date'),
                ('Type', lambda obj: type(obj)),
            ]
        :returns: OrderedDict of {label: (value, param)} that gets dropped
         into the template.
        """

        def follow_path(ob, dotted_attrs):
            new_ob = ob
            attrs = dotted_attrs.split('.')
            for attr in attrs:
                if hasattr(new_ob, attr):
                    new_ob = getattr(new_ob, attr)
                    if callable(new_ob) and not isinstance(new_ob,
                                                           models.Manager):
                        new_ob = new_ob()
                else:
                    raise Exception("Bad dotted attributes passed to %s: %s" %
                                    (type(new_ob), dotted_attrs))
            return new_ob

        details = OrderedDict()
        if not self.get_detail_fields():
            return details
        obj = self.get_object()
        for tupple in self.get_detail_fields():
            label = tupple[0]
            dotted_or_function = tupple[1]
            param = tupple[2] if len(tupple) > 2 else None

            if callable(dotted_or_function):
                new_obj = dotted_or_function(obj)
            else:
                new_obj = follow_path(obj, dotted_or_function)
            details[label] = (new_obj, param)
        return details