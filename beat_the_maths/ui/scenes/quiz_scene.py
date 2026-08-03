from time import perf_counter
from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.answer_result import AnswerResult
from ...core.services.quiz_engine.quiz_config import QuizConfig
from ...core.services.quiz_engine.quiz_engine import QuizEngine
from ..components.text_input import TextInput
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
QUESTION_COLOR = (88, 166, 255)
TEXT_COLOR = (203, 213, 225)
HELP_COLOR = (120, 132, 153)
SUCCESS_COLOR = (74, 222, 128)
FAILURE_COLOR = (248, 113, 113)

FEEDBACK_DURATION = 1.5


class QuizScene(Scene):
    def __init__(
        self,
        app: "PygameApp",
        config: QuizConfig,
    ) -> None:
        super().__init__(app)

        self.engine = QuizEngine(config=config)
        self.problem = self.engine.next_problem()

        self.progress_font = pygame.font.Font(None, 34)
        self.question_font = pygame.font.Font(None, 92)
        self.answer_font = pygame.font.Font(None, 54)
        self.feedback_font = pygame.font.Font(None, 42)
        self.help_font = pygame.font.Font(None, 28)

        self.answer_input = TextInput(
            rect=(440, 390, 400, 80),
            font=self.answer_font,
            placeholder="Ta réponse",
        )

        self.question_started_at = perf_counter()
        self.feedback_result: AnswerResult | None = None
        self.feedback_remaining = 0.0

    def handle_event(self, event: pygame.event.Event) -> None:
        if self.feedback_result is not None:
            return

        submitted = self.answer_input.handle_event(event)

        if submitted:
            duration = perf_counter() - self.question_started_at
            self.feedback_result = self.engine.submit_answer(
                response=self.answer_input.text,
                duration=duration,
            )
            self.feedback_remaining = FEEDBACK_DURATION
            self.answer_input.enabled = False

    def update(self, delta_time: float) -> None:
        if self.feedback_result is None:
            return

        self.feedback_remaining -= delta_time

        if self.feedback_remaining > 0:
            return

        if self.engine.session.is_complete:
            from .results_scene import ResultsScene

            self.app.change_scene(
                ResultsScene(app=self.app, session=self.engine.session)
            )
            return

        self.problem = self.engine.next_problem()
        self.answer_input.clear()
        self.answer_input.enabled = True
        self.feedback_result = None
        self.question_started_at = perf_counter()

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(BACKGROUND_COLOR)

        center_x = surface.get_rect().centerx

        progress = (
            f"Question {self.engine.session.next_question_number}"
            f" / {self.engine.session.config.question_count}"
        )

        self._draw_centered_text(
            surface,
            progress,
            self.progress_font,
            TEXT_COLOR,
            center_x,
            90,
        )

        self._draw_centered_text(
            surface,
            self.problem.question,
            self.question_font,
            QUESTION_COLOR,
            center_x,
            270,
        )

        self.answer_input.draw(surface)

        if self.feedback_result is None:
            feedback_text = "Écris ta réponse puis appuie sur Entrée"
            feedback_color = HELP_COLOR
        elif self.feedback_result.is_correct:
            feedback_text = f"Correct ! {self.feedback_result.duration:.2f} s"
            feedback_color = SUCCESS_COLOR
        else:
            feedback_text = (
                f"Raté ! La réponse était {self.feedback_result.problem.solution}."
            )
            feedback_color = FAILURE_COLOR

        self._draw_centered_text(
            surface,
            feedback_text,
            self.feedback_font,
            feedback_color,
            center_x,
            535,
        )

        self._draw_centered_text(
            surface,
            "Échap : quitter",
            self.help_font,
            HELP_COLOR,
            center_x,
            670,
        )

    @staticmethod
    def _draw_centered_text(
        surface: pygame.Surface,
        text: str,
        font: pygame.font.Font,
        color: tuple[int, int, int],
        center_x: int,
        center_y: int,
    ) -> None:
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect(
            center=(center_x, center_y),
        )
        surface.blit(rendered_text, text_rect)
