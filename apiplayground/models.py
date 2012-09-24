from django.db import models
from django.utils.encoding import smart_unicode

from apiplayground.constants import STATUS_CHOICES, STATUS_OPEN


class Feedback(models.Model):
    """
    Holds Feedback data.
    """
    title = models.CharField(max_length=255)
    resource = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_OPEN)
    duplicate = models.ForeignKey("self", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)