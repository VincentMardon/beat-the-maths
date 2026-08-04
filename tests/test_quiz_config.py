import pytest

from beat_the_maths.core.services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
    QuizConfig,
)


@pytest.mark.parametrize(
    ("difficulty", "expected_maximum"),
    [
        (Difficulty.EASY, 10),
        (Difficulty.MEDIUM, 100),
        (Difficulty.HARD, 1000),
    ],
)
def test_difficulty_defines_maximum_operand(difficulty, expected_maximum):
    assert difficulty.maximum_operand == expected_maximum


def test_numeric_choices_create_expected_enums():
    assert Operation(1) is Operation.ADDITION
    assert Operation(4) is Operation.DIVISION
    assert Difficulty(1) is Difficulty.EASY
    assert Difficulty(3) is Difficulty.HARD


@pytest.mark.parametrize("question_count", [0, -1])
def test_quiz_requires_at_least_one_question(question_count):
    with pytest.raises(
        ValueError,
        match="question_count must be greater than zero",
    ):
        QuizConfig(
            difficulty=Difficulty.EASY,
            operation=Operation.ADDITION,
            question_count=question_count,
        )


def test_quiz_accepts_large_question_count():
    question_count = 10**20

    config = QuizConfig(
        difficulty=Difficulty.HARD,
        operation=Operation.MULTIPLICATION,
        question_count=question_count,
    )

    assert config.question_count == question_count
