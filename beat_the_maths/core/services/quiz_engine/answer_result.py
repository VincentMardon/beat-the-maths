from dataclasses import dataclass

from .problems.problem import Problem


@dataclass(frozen=True, slots=True)
class AnswerResult:
    problem: Problem
    response: str
    duration: float

    @property
    def is_correct(self) -> bool:
        return self.problem.is_correct(self.response)
