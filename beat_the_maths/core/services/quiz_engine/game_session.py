from dataclasses import dataclass, field

from .answer_result import AnswerResult
from .problems.problem import Problem
from .quiz_config import QuizConfig


@dataclass(slots=True)
class GameSession:
    config: QuizConfig
    _results: list[AnswerResult] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

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
        return self.answered_count >= self.config.question_count

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
