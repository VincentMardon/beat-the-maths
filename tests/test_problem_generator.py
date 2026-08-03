import pytest

from beat_the_maths.core.services.quiz_engine import problem_generator
from beat_the_maths.core.services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
)


@pytest.mark.parametrize(
    ("generated_numbers", "operation", "expected_question", "expected_answer"),
    [
        ([2, 3], Operation.ADDITION, "2 + 3 = ? ", 5),
        ([7, 2], Operation.SUBTRACTION, "7 - 2 = ? ", 5),
        ([4, 6], Operation.MULTIPLICATION, "4 x 6 = ? ", 24),
        ([2, 4, 3], Operation.DIVISION, "12 ÷ 4 = ? ", 3),
    ],
)
def test_generates_expected_problem(
    monkeypatch,
    generated_numbers,
    operation,
    expected_question,
    expected_answer,
):
    numbers = iter(generated_numbers)

    monkeypatch.setattr(
        problem_generator,
        "_rand_in_difficulty",
        lambda _difficulty: next(numbers),
    )

    problem = problem_generator.problem_generator(
        difficulty=Difficulty.EASY,
        operation=operation,
    )

    assert problem.question == expected_question
    assert problem.solution == expected_answer


def test_subtraction_never_produces_negative_answer(monkeypatch):
    numbers = iter([2, 7])

    monkeypatch.setattr(
        problem_generator,
        "_rand_in_difficulty",
        lambda _difficulty: next(numbers),
    )

    problem = problem_generator.problem_generator(
        difficulty=Difficulty.EASY,
        operation=Operation.SUBTRACTION,
    )

    assert problem.question == "7 - 2 = ? "
    assert problem.solution == 5
