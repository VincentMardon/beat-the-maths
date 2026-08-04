from ..user_profile import AchievementId, UserProfile
from .quiz_engine.game_session import GameSession


def unlock_achievements(
    profile: UserProfile,
    session: GameSession,
) -> frozenset[AchievementId]:
    newly_unlocked: set[AchievementId] = set()

    if (
        session.is_complete
        and session.config.question_count == 1
        and AchievementId.ONE_QUESTION not in profile.unlocked_achievements
    ):
        profile.unlocked_achievements.add(AchievementId.ONE_QUESTION)
        newly_unlocked.add(AchievementId.ONE_QUESTION)

    return frozenset(newly_unlocked)
