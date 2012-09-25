from django.db import models
from django.utils.encoding import smart_unicode

class ToDo(models.Model):
    """
    Holds To-do data
    """
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField()

    def __unicode__(self):
        return smart_unicode(self.description)