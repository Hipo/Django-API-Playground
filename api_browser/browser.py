import json

from django.conf.urls import url
from django.shortcuts import render_to_response
from django.template import RequestContext

from api_browser.forms import FeedbackForm
from api_browser.settings import API_BROWSER_SCHEMA_PATH


class APIBrowser(object):

    index_template = "api_browser/index.html"
    feedback_template = "api_browser/submit_feedback.html"
    feedback_form = FeedbackForm
    schema = None

    def get_deserializer_module(self):
        return json

    def get_schema(self):
        return self.schema if self.schema is not None else self.load_schema()

    def load_schema(self):
        return self.get_deserializer_module().load(API_BROWSER_SCHEMA_PATH)

    # view logic
    def get_feedback_form(self):
        return self.feedback_form

    def browser_index(self, request):
        return render_to_response(self.index_template, {
           "schema": self.get_schema()
        }, context_instance=RequestContext(request))

    def save_feedback_form(self, request, form):
        form.save()

    def submit_feedback(self, request):
        form = self.get_feedback_form()(request.POST or None)
        if form.is_valid():
            self.save_feedback_form(request, form)
        return render_to_response(self.index_template, {
            "form": form
        }, context_instance=RequestContext(request))


    # urls configuration
    @property
    def urls(self):
        return self.get_urls()

    def get_urls(self):
        return [
            url("^$", self.browser_index, name="api_browser_index"),
            url("^submit-feedback$", self.submit_feedback, name="api_browser_submit_feedback"),
        ]