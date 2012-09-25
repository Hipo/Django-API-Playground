from django.conf import settings

API_PLAYGROUND_SCHEMA_PATH = getattr(settings,
    "API_PLAYGROUND_SCHEMA_PATH", "api_playground_schema.json")