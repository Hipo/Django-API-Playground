import json

from django.conf.urls import url
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext

from apiplayground.forms import FeedbackForm
from apiplayground.settings import API_PLAYGROUND_SCHEMA_PATH


class APIPlayground(object):
    """
    A base class that encapsulates all api browser options.
    """
    index_template = "api_browser/index.html"
    feedback_template = "api_browser/submit_feedback.html"
    feedback_form = FeedbackForm
    schema = None

    def get_serializer(self):
        """
        Returns serialization class or module.
        You can override this method for using other serialization libraries.
        Example:

            # import yaml library at the top of python script.
            def get_serializer(self):
                return yaml

        """
        return json

    def get_schema(self):
        """
        Loads schema file if schema is not defined on the subclass.
        Otherwise, returns the overridden schema from the subclass (example)
        """
        if self.schema is None:
            return self.load_schema()
        return self.schema

    def load_schema(self):
        """
        Loads the schema from file with defined deserialization module.
        """
        return self.get_serializer().load(API_PLAYGROUND_SCHEMA_PATH)

    def browser_index(self, request):
        """
        A view that returns api browser index.
        """
        return render_to_response(self.index_template, {
           "schema": self.get_schema(),
           "feedback_form": self.get_feedback_form(request)
        }, context_instance=RequestContext(request))

    def save_feedback_form(self, request, form):
        """
        Saves feedback data.
        """
        form.save()

    def get_feedback_form(self, request):
        """
        Instantiates feedback form from request.
        """
        return self.feedback_form(request.POST or None)

    def submit_feedback(self, request):
        """
        A view that saves feedback form.
        Returns JSON response.
        """
        form = self.get_feedback_form(request)
        if form.is_valid():
            self.save_feedback_form(request, form)
        if form.errors:
            return self.create_json_response({
                "errors": form.errors
            }, response_class=HttpResponseBadRequest)
        return self.create_json_response({
            "success": True
        })

    def create_json_response(self, data, response_class=HttpResponse):
        """
        A utility method for creating json responses.
        """
        return response_class(json.dumps(data))

    def get_urls(self):
        """
        Returns API Browser URLs.
        You can override method for adding extra views.
        """
        return [
            url("^$", self.browser_index, name="api_playground_index"),
            url("^submit-feedback$", self.submit_feedback, name="api_playground_submit_feedback"),
        ]

    @property
    def urls(self):
        """
        A shortcut property for reaching the urls.
        """
        return self.get_urls()