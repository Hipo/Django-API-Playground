from django.contrib import admin
from apiplayground.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    """Configures admin for Feedback model."""
    list_display = ('title', 'resource', 'status', 'date_created', )
    list_filter = ('status', )
    ordering = ('-date_created', )
admin.site.register(Feedback, FeedbackAdmin)