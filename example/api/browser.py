from api_browser.browser import APIBrowser

class ExampleAPIBrowser(APIBrowser):

    schema = {
        "title": "API Browser",
        "base_url": "http://localhost/api/",
        "resources": [
            {
                "name": "/todos",
                "endpoints": [
                    {
                        "method": "GET",
                        "url": "/api/todos",
                        "description": "Returns all to-do items"
                    },
                    {
                        "method": "POST",
                        "url": "/api/todos",
                        "description": "Creates new to-do item",
                        "parameters": [("description", "text"), ("is_completed", "boolean")]
                    },
                    {
                        "method": "PUT",
                        "url": "/api/todos",
                        "description": "Updates specific todo item",
                        "parameters": [("description", "text"), ("is_completed", "boolean")]
                    },
                    {
                        "method": "DELETE",
                        "url": "/api/todos",
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
                "endpoints": [
                    {
                        "method": "GET",
                        "url": "/api/links",
                        "description": "Returns all links"
                    },
                    {
                        "method": "POST",
                        "url": "/api/links",
                        "description": "Creates new link item"
                    }
                ]
            }
        ]
    }