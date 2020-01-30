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
        })
        return context