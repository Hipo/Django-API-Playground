import re

from django import template, forms

register = template.Library()

@register.assignment_tag()
def get_url_parameters(url):
    pattern = re.compile("(\{([a-z-]+)\})")
    return pattern.findall(url) or ()


TYPE_WIDGET_MAPPING = {
    "string": lambda: forms.TextInput(),
    "boolean": lambda: forms.Select(choices=(
        ("", "None"),
        ("true", "True"),
        ("false", "False")
    ))
}

@register.assignment_tag()
def build_parameter_form(parameters):
    form_fields = {}
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


    return type("ParameterForm", (forms.Form,), form_fields)