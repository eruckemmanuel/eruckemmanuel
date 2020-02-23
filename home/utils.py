from django.utils.translation import gettext as _

status_codes = {
    200:_('OK'),
    201:_('CREATED'),
    202:_('ACCEPTED'),
    404: _('NOT FOUND'),
    401:_('UNAUTHORIZED'),
    403:_('FORBIDDEN'),
    406:_('NOT ACCEPTABLE'),
    430:_('NOT ENOUGH PARAMETERS'),
    500:_('INTERNAL ERROR'),
    560:_('DOMAIN SETUP ERROR. SETUP NOT COMPLETED'),
}