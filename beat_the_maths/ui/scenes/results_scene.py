from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.game_session import GameSession
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
SCORE_COLOR = (88, 166, 255)
TEXT_COLOR = (203, 213, 225)
HELP_COLOR = (120, 132, 153)


class ResultsScene(Scene):
    def __init__(
        self,
        app: "PygameApp",
        session: GameSession,
    ) -> None:
        super().__init__(app)

        self.session = session

        self.title_font = pygame.font.Font(None, 72)
        self.score_font = pygame.font.Font(None, 110)
        self.text_font = pygame.font.Font(None, 34)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_RETURN:
            from .configuration_scene import ConfigurationScene

            self.app.change_scene(ConfigurationScene(self.app))
        elif event.key == pygame.K_BACKSPACE:
            from .title_scene import TitleScene

            self.app.change_scene(TitleScene(self.app))

    def update(self, _delta_time: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(BACKGROUND_COLOR)

        center_x = surface.get_rect().centerx

        self._draw_centered_text(
            surface,
            "PARTIE TERMINÉE",
            self.title_font,
            TITLE_COLOR,
            center_x,
            160,
        )

        score_text = f"{self.session.score} / {self.session.config.question_count}"

        self._draw_centered_text(
            surface,
            score_text,
            self.score_font,
            SCORE_COLOR,
            center_x,
            330,
        )

        self._draw_centered_text(
            surface,
            "Entrée : rejouer",
            self.text_font,
            TEXT_COLOR,
            center_x,
            500,
        )

        self._draw_centered_text(
            surface,
            "Retour arrièere : écran titre    •    Échap : quitter",
            self.text_font,
            HELP_COLOR,
            center_x,
            650,
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
