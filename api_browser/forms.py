from django import forms

from api_browser.models import Feedback


class FeedbackForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        "required": "required"
    }))

    class Meta:
        model = Feedback
        exclude = ("duplicate", "status")