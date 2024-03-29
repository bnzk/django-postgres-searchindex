from django.conf import settings

POSTGRES_SEARCHINDEX = getattr(
    settings,
    "POSTGRES_SEARCHINDEX",
    {
        "default": {},
    },
)

LANGUAGE_2_PGCONFIG = getattr(
    settings,
    "POSTGRES_SEARCHINDEX_LANGUAGE_2_PGCONFIG",
    {
        "en": "english",
        "de": "german",
        "fr": "french",
    },
)

USE_CMS_INDEX = getattr(
    settings,
    "POSTGRES_SEARCHINDEX_USE_CMS_INDEX",
    True,
)
