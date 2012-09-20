import json

from django.conf.urls import url
from django.shortcuts import render_to_response
from django.template import RequestContext
from settings import API_BROWSER_SCHEMA_PATH


class APIBrowser(object):

    index_template = "api_browser/index.html"
    schema = None

    @property
    def urls(self):
        return self.get_urls()

    def get_urls(self):
        return [
            url("^$", self.browser_index, name="api_browser_index")
        ]

    def get_schema(self):
        return self.schema if self.schema is not None else self.load_schema()

    def load_schema(self):
        return self.get_deserializer_module().load(API_BROWSER_SCHEMA_PATH)

    def browser_index(self, request):
        return render_to_response(self.index_template, {
           "schema": self.get_schema()
        }, context_instance=RequestContext(request))

    def get_deserializer_module(self):
        return json