from ....data.texts.parameters import DIFFICULTY_LEVEL, EXERCISE_TYPE
from ...services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
    QuizConfig,
)
from ..outputs.game import print_invalid_input_msg


def input_params() -> QuizConfig:
    while True:
        try:
            operation = Operation(int(input(EXERCISE_TYPE).strip()))
            break
        except ValueError:
            print_invalid_input_msg(maximum=len(Operation))

    while True:
        try:
            difficulty = Difficulty(int(input(DIFFICULTY_LEVEL).strip()))
            break
        except ValueError:
            print_invalid_input_msg(maximum=len(Difficulty))

    return QuizConfig(difficulty=difficulty, operation=operation)
