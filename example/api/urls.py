from django.conf.urls import include, patterns

from todos.resources import ToDoResource
from api.playgrounds import ExampleAPIPlayground
from api.resources import FeedbackResource


urlpatterns = patterns('',

    (r'^', include(FeedbackResource().urls)),
    (r'^', include(ToDoResource().urls)),

)