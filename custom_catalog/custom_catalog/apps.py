"""
custom_catalog Django application initialization.
"""

from django.apps import AppConfig


class CustomCatalogConfig(AppConfig):
    """
    Configuration for the custom_catalog Django application.
    """

    name = 'custom_catalog'

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "custom-catalog",
                "regex": rf"custom-catalog/",
                "relative_path": "urls",
            },
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings"},
                "test": {"relative_path": "settings"},
                "production": {"relative_path": "settings"},
            },
            "cms.djangoapp": {
                "common": {"relative_path": "settings"},
                "test": {"relative_path": "settings"},
                "production": {"relative_path": "settings"},
            },
        },
    }
