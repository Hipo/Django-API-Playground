from django.conf.urls import patterns, include, url

from api.playgrounds import ExampleAPIPlayground


urlpatterns = patterns('',

    (r'^api/', include("api.urls")),

    # api playground
    (r'^', include(ExampleAPIPlayground().urls)),

)
