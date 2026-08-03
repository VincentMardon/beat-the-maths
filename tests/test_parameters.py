from beat_the_maths.core.io.inputs.parameters import input_params
from beat_the_maths.core.services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
    QuizConfig,
)


def test_input_params_returns_quiz_config(monkeypatch):
    answers = iter(["1", "2"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _prompt: next(answers),
    )

    config = input_params()

    assert config == QuizConfig(
        difficulty=Difficulty.MEDIUM,
        operation=Operation.ADDITION,
    )


def test_input_params_retries_invalid_choices(monkeypatch, capsys):
    answers = iter(
        [
            "invalid",
            "5",
            "4",
            "0",
            "3",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _prompt: next(answers),
    )

    config = input_params()

    assert config == QuizConfig(
        difficulty=Difficulty.HARD,
        operation=Operation.DIVISION,
    )

    output = capsys.readouterr().out
    assert output.count("Invalid input") == 3
