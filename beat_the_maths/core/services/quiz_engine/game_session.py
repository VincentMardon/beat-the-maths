from dataclasses import dataclass, field

from .answer_result import AnswerResult
from .problems.problem import Problem


@dataclass(slots=True)
class GameSession:
    difficulty_level: int
    exercise_type: int
    question_count: int = 10
    _results: list[AnswerResult] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        if self.question_count <= 0:
            raise ValueError("question_count must be greater than zero")

    @property
    def results(self) -> tuple[AnswerResult, ...]:
        return tuple(self._results)

    @property
    def answered_count(self) -> int:
        return len(self._results)

    @property
    def score(self) -> int:
        return sum(result.is_correct for result in self._results)

    @property
    def next_question_number(self) -> int:
        return self.answered_count + 1

    @property
    def is_complete(self) -> bool:
        return self.answered_count >= self.question_count

    def record_answer(
        self,
        problem: Problem,
        response: str,
        duration: float,
    ) -> AnswerResult:
        if self.is_complete:
            raise RuntimeError("cannot record an answer in a completed session")

        result = AnswerResult(
            problem=problem,
            response=response,
            duration=duration,
        )
        self._results.append(result)
        return result
