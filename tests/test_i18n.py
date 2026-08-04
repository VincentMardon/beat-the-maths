from beat_the_maths.i18n import (
    CATALOGS,
    Language,
    Text,
    translate,
)
from beat_the_maths.ui.app_settings import AppSettings


def test_every_language_defines_every_text():
    expected_texts = set(Text)

    for language in Language:
        assert set(CATALOGS[language]) == expected_texts


def test_translation_formats_dynamic_values():
    translated = translate(
        Language.ENGLISH,
        Text.QUIZ_PROGRESS,
        current=3,
        total=10,
    )

    assert translated == "Question 3 / 10"


def test_french_is_the_default_language():
    assert AppSettings().language is Language.FRENCH
