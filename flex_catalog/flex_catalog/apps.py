"""
flex_catalog Django application initialization.
"""

from django.apps import AppConfig


class FlexCatalogConfig(AppConfig):
    """
    Configuration for the flex_catalog Django application.
    """

    name = 'flex_catalog'

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "flex-catalog",
                "regex": rf"flex-catalog/",
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