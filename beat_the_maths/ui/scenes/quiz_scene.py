from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.quiz_config import QuizConfig
from ...core.services.quiz_engine.quiz_engine import QuizEngine
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
QUESTION_COLOR = (88, 166, 255)
TEXT_COLOR = (203, 213, 225)
HELP_COLOR = (120, 132, 153)


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
        self.text_font = pygame.font.Font(None, 32)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            from .configuration_scene import ConfigurationScene

            self.app.change_scene(ConfigurationScene(self.app))

    def update(self, _delta_time: float) -> None:
        pass

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
            310,
        )

        self._draw_centered_text(
            surface,
            "La saisie de la réponse arrive à la prochaine étape",
            self.text_font,
            HELP_COLOR,
            center_x,
            450,
        )

        self._draw_centered_text(
            surface,
            "Retour arrière : abandonner la partie    •    Échap : quitter",
            self.text_font,
            HELP_COLOR,
            center_x,
            660,
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
