from dataclasses import dataclass, field
from enum import StrEnum


class AchievementId(StrEnum):
    ONE_QUESTION = "one_question"


@dataclass(slots=True)
class UserProfile:
    unlocked_achievements: set[AchievementId] = field(
        default_factory=set,
    )
