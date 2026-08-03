from collections.abc import Callable

from .answer_result import AnswerResult
from .game_session import GameSession
from .problem_generator import problem_generator
from .problems.problem import Problem
from .quiz_config import Difficulty, Operation, QuizConfig

ProblemFactory = Callable[[Difficulty, Operation], Problem]


class QuizEngine:
    def __init__(
        self,
        config: QuizConfig,
        problem_factory: ProblemFactory = problem_generator,
    ) -> None:
        self.session = GameSession(config=config)
        self._problem_factory = problem_factory
        self._current_problem: Problem | None = None

    @property
    def current_problem(self) -> Problem | None:
        return self._current_problem

    def next_problem(self) -> Problem:
        if self.session.is_complete:
            raise RuntimeError("cannot generate a problem for a completed session")

        if self._current_problem is None:
            self._current_problem = self._problem_factory(
                self.session.config.difficulty,
                self.session.config.operation,
            )

        return self._current_problem

    def submit_answer(
        self,
        response: str,
        duration: float,
    ) -> AnswerResult:
        if self._current_problem is None:
            raise RuntimeError("cannot submit an answer without a current problem")

        result = self.session.record_answer(
            problem=self._current_problem,
            response=response,
            duration=duration,
        )
        self._current_problem = None
        return result
