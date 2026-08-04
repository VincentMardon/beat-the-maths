from time import perf_counter
from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.answer_result import AnswerResult
from ...core.services.quiz_engine.quiz_config import QuizConfig
from ...core.services.quiz_engine.quiz_engine import QuizEngine
from ..components.text_input import TextInput
from ..drawing import draw_text
from ..theme import THEME, get_font
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

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

        self.progress_font = get_font(34)
        self.question_font = get_font(92)
        self.answer_font = get_font(54)
        self.feedback_font = get_font(42)
        self.help_font = get_font(28)

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
            self.app.show_results(self.engine.session)
            return

        self.problem = self.engine.next_problem()
        self.answer_input.clear()
        self.answer_input.enabled = True
        self.feedback_result = None
        self.question_started_at = perf_counter()

    def draw_content(self, surface: pygame.Surface) -> None:
        center_x = surface.get_rect().centerx

        progress = (
            f"Question {self.engine.session.next_question_number}"
            f" / {self.engine.session.config.question_count}"
        )

        draw_text(
            surface,
            progress,
            self.progress_font,
            THEME.text_secondary,
            center=(center_x, 90),
        )

        draw_text(
            surface,
            self.problem.question,
            self.question_font,
            THEME.accent,
            center=(center_x, 270),
        )

        self.answer_input.draw(surface)

        if self.feedback_result is None:
            feedback_text = "Écris ta réponse puis appuie sur Entrée"
            feedback_color = THEME.text_muted
        elif self.feedback_result.is_correct:
            feedback_text = f"Correct ! {self.feedback_result.duration:.2f} s"
            feedback_color = THEME.success
        else:
            feedback_text = (
                f"Raté ! La réponse était {self.feedback_result.problem.solution}."
            )
            feedback_color = THEME.failure

        draw_text(
            surface,
            feedback_text,
            self.feedback_font,
            feedback_color,
            center=(center_x, 535),
        )

        draw_text(
            surface,
            "Échap : quitter",
            self.help_font,
            THEME.text_muted,
            center=(center_x, 670),
        )
