from django.conf.urls.defaults import *

from api.browser import ExampleAPIBrowser

from links.resources import LinksResource
from todos.resources import ToDoResource


urlpatterns = patterns('',

    (r'^', include(ToDoResource().urls)),
    (r'^', include(LinksResource().urls)),
    (r'browser', include(ExampleAPIBrowser().urls)),


)