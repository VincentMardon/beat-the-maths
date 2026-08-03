import pytest

from beat_the_maths.core.services.quiz_engine.problems.problem import Problem
from beat_the_maths.core.services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
    QuizConfig,
)
from beat_the_maths.core.services.quiz_engine.quiz_engine import QuizEngine


def make_config(question_count: int = 1) -> QuizConfig:
    return QuizConfig(
        difficulty=Difficulty.EASY,
        operation=Operation.ADDITION,
        question_count=question_count,
    )


def test_engine_runs_a_complete_question():
    problem = Problem(question="2 + 3 = ? ", solution=5)

    def problem_factory(difficulty, operation):
        assert difficulty is Difficulty.EASY
        assert operation is Operation.ADDITION
        return problem

    engine = QuizEngine(
        config=make_config(),
        problem_factory=problem_factory,
    )

    generated_problem = engine.next_problem()
    result = engine.submit_answer(
        response="5",
        duration=1.25,
    )

    assert generated_problem is problem
    assert result.problem is problem
    assert result.is_correct
    assert engine.current_problem is None
    assert engine.session.score == 1
    assert engine.session.is_complete


def test_engine_keeps_current_problem_until_answered():
    problem = Problem(question="2 + 3 = ? ", solution=5)
    generation_count = 0

    def problem_factory(_difficulty, _operation):
        nonlocal generation_count
        generation_count += 1
        return problem

    engine = QuizEngine(
        config=make_config(),
        problem_factory=problem_factory,
    )

    first_problem = engine.next_problem()
    second_problem = engine.next_problem()

    assert first_problem is second_problem
    assert generation_count == 1


def test_engine_rejects_answer_without_current_peoblem():
    engine = QuizEngine(config=make_config())

    with pytest.raises(
        RuntimeError, match="cannot submit an answer without a current problem"
    ):
        engine.submit_answer(response="5", duration=1.0)


def test_engine_rejects_problem_after_completion():
    problem = Problem(question="2 + 3 = ? ", solution=5)

    engine = QuizEngine(
        config=make_config(),
        problem_factory=lambda _difficulty, _operation: problem,
    )

    engine.next_problem()
    engine.submit_answer(
        response="5",
        duration=1.0,
    )

    with pytest.raises(
        RuntimeError,
        match="cannot generate a problem for a completed session",
    ):
        engine.next_problem()
