from django import template
from apiplayground.forms import build_url_form, build_data_form

register = template.Library()


@register.assignment_tag()
def get_endpoint_forms(endpoint):
    url_parameter_form = build_url_form(endpoint.get("url", ""))
    data_parameter_form = build_data_form(endpoint.get("parameters", []))

    return {
        "url_parameter_form": url_parameter_form,
        "data_parameter_form": data_parameter_form
    }