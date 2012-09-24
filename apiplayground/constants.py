from django.utils.translation import ugettext_lazy as _

STATUS_OPEN = 0
STATUS_CLOSED = 1

STATUS_CHOICES = (
    (STATUS_OPEN, _('Open')),
    (STATUS_CLOSED, _('Closed')),
)