import pytest

from beat_the_maths.core.services.quiz_engine import problem_generator


@pytest.mark.parametrize(
    ("generated_numbers", "exercise_type", "expected_question", "expected_answer"),
    [
        ([2, 3], 1, "2 + 3 = ? ", 5),
        ([7, 2], 2, "7 - 2 = ? ", 5),
        ([4, 6], 3, "4 x 6 = ? ", 24),
        ([2, 4, 3], 4, "12 ÷ 4 = ? ", 3),
    ],
)
def test_generates_expected_problem(
    monkeypatch,
    generated_numbers,
    exercise_type,
    expected_question,
    expected_answer,
):
    numbers = iter(generated_numbers)

    monkeypatch.setattr(
        problem_generator, "_rand_in_level", lambda _level: next(numbers)
    )

    question, answer = problem_generator.problem_generator(
        difficulty_level=1,
        exercise_type=exercise_type,
    )

    assert question == expected_question
    assert answer == expected_answer


def test_subtraction_never_produces_negative_answer(monkeypatch):
    numbers = iter([2, 7])

    monkeypatch.setattr(
        problem_generator,
        "_rand_in_level",
        lambda _level: next(numbers),
    )

    question, answer = problem_generator.problem_generator(
        difficulty_level=1,
        exercise_type=2,
    )

    assert question == "7 - 2 = ? "
    assert answer == 5


def test_unknown_exercise_type_falls_back_to_addition(monkeypatch):
    numbers = iter([2, 3])

    monkeypatch.setattr(
        problem_generator, "_rand_in_level", lambda _level: next(numbers)
    )

    question, answer = problem_generator.problem_generator(
        difficulty_level=1,
        exercise_type=99,
    )

    assert question == "2 + 3 = ? "
    assert answer == 5
