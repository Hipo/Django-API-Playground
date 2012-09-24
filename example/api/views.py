from apiplayground.browser import APIBrowser

class ExampleAPIBrowser(APIBrowser):

    schema = {
        "title": "API Browser",
        "base_url": "http://localhost/api/",
        "resources": [
            {
                "name": "/todos",
                "description": "This resource allows you to manage todo items.",
                "endpoints": [
                    {
                        "method": "GET",
                        "url": "/api/todos/",
                        "description": "Returns all to-do items"
                    },
                    {
                        "method": "POST",
                        "url": "/api/todos/",
                        "description": "Creates new to-do item",
                        "parameters": [{
                            "name": "description",
                            "type": "string",
                            "is_required": True
                        }, {
                            "name": "is_completed",
                            "type": "boolean"
                        }]
                    },
                    {
                        "method": "PUT",
                        "url": "/api/todos/{todo-id}",
                        "description": "Updates specific todo item",
                        "parameters": [{
                            "name": "description",
                            "type": "string",
                            "is_required": True,
                            "description": "the to-do item"
                            }, {
                            "name": "is_completed",
                            "type": "boolean",
                            "description": "status of to-do item"
                       }]
                    },
                    {
                        "method": "DELETE",
                        "url": "/api/todos/",
                        "description": "Removes all to-do items"
                    },
                    {
                        "method": "GET",
                        "url": "/api/todos/{todo-id}",
                        "description": "Returns specific todo item."
                    }
                ]
            },
            {
                "name": "/links",
                "description": "This resource allows you to manage links.",
                "endpoints": [
                    {
                        "method": "GET",
                        "url": "/api/links/",
                        "description": "Returns all links"
                    },
                    {
                        "method": "POST",
                        "url": "/api/links/",
                        "description": "Creates new link item"
                    }
                ]
            }
        ]
    }