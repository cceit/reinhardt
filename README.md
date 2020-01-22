# Reinhardt
A collection of Django helpers designed for ease-of-use and rapid development

# Installation

    pip install git+https://github.com/cceit/reinhardt.git
    
Add required apps to installed apps:

```python
INSTALLED_APPS = [
    ...
    'django_tables2',
    'widget_tweaks',
    'crispy_forms',
    'rules',
    'reinhardt'
]
```

Add Rules authentication backend:

```python
AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend'
)
```
    
# Models

We utilize the Rules package to define permission on our models like so:

```python
    import rules
    from reinhardt.models import AuditModel

    class Book(AuditModel):
        class Meta:
            rules_permissions = {
                'add': rules.is_staff,
                'change': rules.is_staff,
                'delete': rules.is_staff,
                'view': rules.is_staff,
                'view_list': rules.is_staff
            }
```
            
            
# Views

The corresponding Reinhardt Views will automatically check appropriate permissions based on the naming convention above, but this can also be customized on a per view basis like so, provided the permission_required matches a rules_permission defined on the model:
```python
class Book(AuditModel):
    class Meta:
        rules_permissions = {
            'create': rules.is_staff
        }
        
class BookCreateView(ReinhardtCreateView):
     model = Book
     form_class = BookCreateForm
     permission_required = 'create'
```
    

