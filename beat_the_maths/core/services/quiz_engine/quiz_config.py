from dataclasses import dataclass
from enum import IntEnum


class Operation(IntEnum):
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4


class Difficulty(IntEnum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

    @property
    def maximum_operand(self) -> int:
        return 10**self.value


@dataclass(frozen=True, slots=True)
class QuizConfig:
    difficulty: Difficulty
    operation: Operation
    question_count: int = 10

    def __post_init__(self) -> None:
        if self.question_count <= 0:
            raise ValueError("question_count must be greater than zero")
