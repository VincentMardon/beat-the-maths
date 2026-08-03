import pytest

from beat_the_maths.core.services.quiz_engine.game_session import GameSession
from beat_the_maths.core.services.quiz_engine.problems.problem import Problem


def test_new_session_has_no_results():
    session = GameSession(
        difficulty_level=1,
        exercise_type=1,
    )

    assert session.results == ()
    assert session.answered_count == 0
    assert session.score == 0
    assert session.next_question_number == 1
    assert not session.is_complete


def test_session_records_answers_and_calculates_score():
    session = GameSession(
        difficulty_level=1,
        exercise_type=1,
        question_count=2,
    )
    problem = Problem(question="2 + 3 = ? ", solution=5)

    first_result = session.record_answer(
        problem=problem,
        response="5",
        duration=1.25,
    )
    second_result = session.record_answer(
        problem=problem,
        response="4",
        duration=2.5,
    )

    assert first_result.is_correct
    assert not second_result.is_correct
    assert session.results == (first_result, second_result)
    assert session.answered_count == 2
    assert session.score == 1
    assert session.is_complete


def test_session_rejects_answer_after_completion():
    session = GameSession(
        difficulty_level=1,
        exercise_type=1,
        question_count=1,
    )
    problem = Problem(question="2 + 3 = ? ", solution=5)

    session.record_answer(
        problem=problem,
        response="5",
        duration=1.25,
    )

    with pytest.raises(
        RuntimeError,
        match="cannot record an answer in a completed session",
    ):
        session.record_answer(
            problem=problem,
            response="5",
            duration=1.0,
        )


@pytest.mark.parametrize("question_count", [0, -1])
def test_session_requires_at_least_one_question(question_count):
    with pytest.raises(
        ValueError,
        match="question_count must be greater than zero",
    ):
        GameSession(
            difficulty_level=1,
            exercise_type=1,
            question_count=question_count,
        )
