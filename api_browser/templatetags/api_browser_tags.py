from django.utils.datastructures import SortedDict
import re

from django import template, forms

register = template.Library()

TYPE_WIDGET_MAPPING = {
    "string": forms.TextInput,
    "boolean": forms.CheckboxInput
}

def tokenize_url_parameters(url):
    pattern = re.compile("(\{([a-z-]+)\})")
    return pattern.findall(url) or ()


def build_data_form(parameters):
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
    form_fields = SortedDict()
    url_parameters = tokenize_url_parameters(url)
    for token, parameter in url_parameters:
        form_fields["url-parameter-%s" % parameter] = forms.CharField(
            label=parameter, widget=forms.TextInput(attrs={
                "required": "required",
                "data-token": token,
            }))

    return type("URLParameterForm", (forms.Form,), form_fields)


@register.assignment_tag()
def get_endpoint_forms(endpoint):
    url_parameter_form = build_url_form(endpoint.get("url", ""))
    data_parameter_form = build_data_form(endpoint.get("parameters", []))

    return {
        "url_parameter_form": url_parameter_form,
        "data_parameter_form": data_parameter_form
    }