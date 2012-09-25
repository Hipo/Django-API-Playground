from django.conf.urls.defaults import *

from todos.resources import ToDoResource
from links.resources import LinksResource
from api.playgrounds import ExampleAPIPlayground


urlpatterns = patterns('',

    (r'^', include(ToDoResource().urls)),
    (r'^', include(LinksResource().urls)),
    (r'browser/', include(ExampleAPIPlayground().urls)),

)