from django import forms
from django.utils.datastructures import SortedDict

from apiplayground.models import Feedback
from apiplayground.utils import tokenize_url_parameters


class FeedbackForm(forms.ModelForm):
    """
    A form that updates and creates feedbacks.
    """
    title = forms.CharField(widget=forms.TextInput(attrs={
        "required": "required"
    }))

    class Meta:
        model = Feedback
        exclude = ("duplicate", "status")

TYPE_WIDGET_MAPPING = {
    "string": forms.TextInput,
    "boolean": forms.CheckboxInput
}

def build_data_form(parameters):
    """
    Builds a form with given parameters as dynamically.
    """
    form_fields = SortedDict()
    for parameter in parameters:
        parameter_name = parameter.get("name")
        parameter_type = parameter.get("type", "string") # default type is "string"
        is_required = parameter.get("is_required", False)
        form_widget = TYPE_WIDGET_MAPPING.get(parameter_type)

        assert "name" in parameter, "Parameter name is required"
        assert form_widget is not None, "Wrong field type."

        widget = form_widget()
        form_fields[parameter_name] = forms.CharField(
            label=parameter_name, widget=widget)

        if is_required:
            widget.attrs["required"] = "required"

    return type("DataParameterForm", (forms.Form,), form_fields)


def build_url_form(url):
    """
    Builds a url parameter form from the given url.
    """
    form_fields = SortedDict()
    url_parameters = tokenize_url_parameters(url)
    for token, parameter in url_parameters:
        form_fields["url-parameter-%s" % parameter] = forms.CharField(
            label=parameter, widget=forms.TextInput(attrs={
                "required": "required",
                "data-token": token,
                }))

    return type("URLParameterForm", (forms.Form,), form_fields)