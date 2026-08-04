from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.game_session import GameSession
from ..drawing import draw_text
from ..theme import THEME, get_font
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp


class ResultsScene(Scene):
    def __init__(
        self,
        app: "PygameApp",
        session: GameSession,
    ) -> None:
        super().__init__(app)

        self.session = session

        self.title_font = get_font(72)
        self.score_font = get_font(110)
        self.text_font = get_font(34)

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
        surface.fill(THEME.background)

        center_x = surface.get_rect().centerx

        draw_text(
            surface,
            "PARTIE TERMINÉE",
            self.title_font,
            THEME.heading,
            center=(center_x, 160),
        )

        score_text = f"{self.session.score} / {self.session.config.question_count}"

        draw_text(
            surface,
            score_text,
            self.score_font,
            THEME.accent,
            center=(center_x, 330),
        )

        draw_text(
            surface,
            "Entrée : rejouer",
            self.text_font,
            THEME.text_secondary,
            center=(center_x, 500),
        )

        draw_text(
            surface,
            "Retour arrière : écran titre    •    Échap : quitter",
            self.text_font,
            THEME.text_muted,
            center=(center_x, 650),
        )
