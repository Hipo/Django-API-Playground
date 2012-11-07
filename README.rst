Django API Playground
=====================

A django app that creates api explorer for RESTful APIs.

Works with any RESTful API. For example, you can create api explorer for your tastypie based API with this app.

Demo: `http://api-playground-demo.hipo.biz <http://api-playground-demo.hipo.biz>`_

.. image:: https://github.com/hipo/Django-API-Playground/raw/master/docs/images/api-playground-2.png



Instructions
""""""""""""

To get this application up and running, please follow the steps below:

Install from pip::

    pip install django-api-playground

Or from source::

   pip install git+git://github.com/Hipo/Django-API-Playground.git

Add to installed apps::

    INSTALLED_APPS =(
        # ...

        'apiplayground',
    )

Installation is completed. You can define the API schema now.

First step, Create an url::

    # urls.py

    from api.playgrounds import ExampleAPIPlayground

    urlpatterns = patterns('',
        (r'api-explorer/', include(ExampleAPIPlayground().urls)),
    )

Second step, Define a subclass for your API::

    # api/playgrounds.py

    from apiplayground import APIPlayground

    class ExampleAPIPlayground(APIPlayground):

        schema = {
            "title": "API Playground",
            "base_url": "http://localhost/api/",
            "resources": [
                {
                    "name": "/feedbacks",
                    "description": "This resource allows you to manage feedbacks.",
                    "endpoints": [
                        {
                            "method": "GET",
                            "url": "/api/feedbacks/{feedback-id}",
                            "description": "Returns a specific feedback item",
                            "parameters": [{
                                "name": "order_by",
                                "type": "select",
                                "choices": [["", "None"], ["id", "id"], ["-id", "-id"]],
                                "default": "id"
                            }]
                        },
                        {
                            "method": "POST",
                            "url": "/api/feedbacks/",
                            "description": "Creates new feedback item",
                            "parameters": [{
                                "name": "title",
                                "type": "string"
                            },
                            {
                                "name": "resource",
                                "type": "string"
                            },
                            {
                               "name": "description",
                               "type": "string"
                            }]
                        }
                    ]
                },
            ]
        }

That's all. More detailed documentation will be coming soon.

Special Thanks
==============

 - Berker Peksag (for such a beautiful project name suggestion)
