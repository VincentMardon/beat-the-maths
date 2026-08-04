from dataclasses import dataclass

from ..i18n import Language


@dataclass(slots=True)
class AppSettings:
    language: Language = Language.FRENCH
