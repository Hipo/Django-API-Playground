from django.db import models
from django.utils.encoding import smart_unicode

class Link(models.Model):
    """
    Holds link data
    """
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return smart_unicode(self.title)