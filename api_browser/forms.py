from django import forms

from api_browser.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback