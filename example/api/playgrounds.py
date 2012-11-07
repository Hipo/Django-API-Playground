from apiplayground import APIPlayground

class ExampleAPIPlayground(APIPlayground):

    schema = {
        "title": "API Playground",
        "base_url": "http://localhost/api/",
        "resources": [
            {
                "name": "/todos",
                "description": "This resource allows you to manage todo items.",
                "endpoints": [
                    {
                        "method": "GET",
                        "url": "/api/todos/",
                        "description": "Returns all to-do items",
                        "parameters": [{
                            "name": "order_by",
                            "type": "select",
                            "choices": [["", "None"], ["id", "id"], ["-id", "-id"]],
                            "default": "id"
                        }]
                    },
                    {
                        "method": "GET",
                        "url": "/api/todos/{todo-id}",
                        "description": "Returns specific todo item."
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
                        "description": "Replaces specific todo item",
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
                        "method": "PATCH",
                        "url": "/api/todos/{todo-id}",
                        "description": "Updates specific todo items",
                        "parameters": [{
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
                        "method": "DELETE",
                        "url": "/api/todos/{todo-id}",
                        "description": "Removes specific to-do item"
                    },
                ]
            },
            {
                "name": "/feedbacks",
                "description": "This resource allows you to manage feedbacks.",
                "endpoints": [
                    {
                        "method": "GET",
                        "url": "/api/feedbacks/",
                        "description": "Returns all feedback items"
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
            }
        ]
    }
