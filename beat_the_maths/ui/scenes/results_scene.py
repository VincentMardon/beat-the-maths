from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.game_session import GameSession
from ...core.user_profile import AchievementId
from ...i18n import Text
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
        newly_unlocked: frozenset[AchievementId],
    ) -> None:
        super().__init__(app)

        self.session = session
        self.newly_unlocked = newly_unlocked

        self.title_font = get_font(72)
        self.score_font = get_font(110)
        self.text_font = get_font(34)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_RETURN:
            self.app.show_configuration()
        elif event.key == pygame.K_BACKSPACE:
            self.app.show_title()

    def draw_content(self, surface: pygame.Surface) -> None:
        center_x = surface.get_rect().centerx

        draw_text(
            surface,
            self.app.translate(Text.RESULTS_TITLE),
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
            self.app.translate(Text.RESULTS_REPLAY),
            self.text_font,
            THEME.text_secondary,
            center=(center_x, 500),
        )

        draw_text(
            surface,
            self.app.translate(Text.RESULTS_BACK_TO_TITLE),
            self.text_font,
            THEME.text_muted,
            center=(center_x, 650),
        )
