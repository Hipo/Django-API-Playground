from django.conf import settings

API_BROWSER_SCHEMA_PATH = getattr(settings,
    "API_BROWSER_SCHEMA_PATH", "api_browser_schema.json")