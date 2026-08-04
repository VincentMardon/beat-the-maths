from beat_the_maths.core.services.achievement_engine import (
    unlock_achievements,
)
from beat_the_maths.core.services.quiz_engine.game_session import GameSession
from beat_the_maths.core.services.quiz_engine.problems.problem import Problem
from beat_the_maths.core.services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
    QuizConfig,
)
from beat_the_maths.core.user_profile import AchievementId, UserProfile


def make_session(question_count: int) -> GameSession:
    config = QuizConfig(
        difficulty=Difficulty.EASY,
        operation=Operation.ADDITION,
        question_count=question_count,
    )
    return GameSession(config=config)


def complete_session(session: GameSession) -> None:
    problem = Problem(question="2 + 3 = ? ", solution=5)

    while not session.is_complete:
        session.record_answer(
            problem=problem,
            response="5",
            duration=1.0,
        )


def test_unlocks_one_question_achievement():
    profile = UserProfile()
    session = make_session(question_count=1)
    complete_session(session)

    newly_unlocked = unlock_achievements(profile, session)

    assert newly_unlocked == frozenset({AchievementId.ONE_QUESTION})
    assert profile.unlocked_achievements == {AchievementId.ONE_QUESTION}


def test_does_not_unlock_achievement_before_session_is_complete():
    profile = UserProfile()
    session = make_session(question_count=1)

    newly_unlocked = unlock_achievements(profile, session)

    assert newly_unlocked == frozenset()
    assert profile.unlocked_achievements == set()


def test_does_not_unlock_achievements_for_longer_session():
    profile = UserProfile()
    session = make_session(question_count=2)
    complete_session(session)

    newly_unlocked = unlock_achievements(profile, session)

    assert newly_unlocked == frozenset()
    assert profile.unlocked_achievements == set()


def test_does_not_report_an_already_unlocked_achievement_twice():
    profile = UserProfile()
    session = make_session(question_count=1)
    complete_session(session)

    first_unlock = unlock_achievements(profile, session)
    second_unlock = unlock_achievements(profile, session)

    assert first_unlock == frozenset({AchievementId.ONE_QUESTION})
    assert second_unlock == frozenset()
