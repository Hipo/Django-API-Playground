from django import forms

from apiplayground.models import Feedback


class FeedbackForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        "required": "required"
    }))

    class Meta:
        model = Feedback
        exclude = ("duplicate", "status")