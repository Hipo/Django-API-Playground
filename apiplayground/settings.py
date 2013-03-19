from django.conf import settings

API_PLAYGROUND_SCHEMA_PATH = getattr(settings,
    "API_PLAYGROUND_SCHEMA_PATH", "api_playground_schema.json")

# Toggle the feedback form
API_PLAYGROUND_FEEDBACK = getattr(settings,
    "API_PLAYGROUND_FEEDBACK", True)
