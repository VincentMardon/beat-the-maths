from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.game_session import GameSession
from ...core.user_profile import AchievementId
from ...i18n import Text
from ..achievement_icons import load_achievement_icon
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
        self.achievement_label_font = get_font(26)
        self.achievement_name_font = get_font(42)
        self.achievement_description_font = get_font(28)

        self.achievement_icon: pygame.Surface | None = None
        if AchievementId.ONE_QUESTION in self.newly_unlocked:
            self.achievement_icon = load_achievement_icon(AchievementId.ONE_QUESTION)

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
            center=(center_x, 85),
        )

        score_text = f"{self.session.score} / {self.session.config.question_count}"

        draw_text(
            surface,
            score_text,
            self.score_font,
            THEME.accent,
            center=(center_x, 220),
        )

        if self.achievement_icon is not None:
            achievement_rect = pygame.Rect(250, 320, 780, 210)

            pygame.draw.rect(
                surface,
                THEME.surface,
                achievement_rect,
                border_radius=20,
            )
            pygame.draw.rect(
                surface,
                THEME.border_selected,
                achievement_rect,
                width=2,
                border_radius=20,
            )

            icon_rect = self.achievement_icon.get_rect(
                center=(360, achievement_rect.centery)
            )
            surface.blit(self.achievement_icon, icon_rect)

            text_center_x = 730

            draw_text(
                surface,
                self.app.translate(Text.ACHIEVEMENT_UNLOCKED),
                self.achievement_label_font,
                THEME.success,
                center=(text_center_x, 365),
            )

            draw_text(
                surface,
                self.app.translate(Text.ACHIEVEMENT_ONE_QUESTION_NAME),
                self.achievement_name_font,
                THEME.heading,
                center=(text_center_x, 420),
            )

            draw_text(
                surface,
                self.app.translate(Text.ACHIEVEMENT_ONE_QUESTION_DESCRIPTION),
                self.achievement_description_font,
                THEME.text_secondary,
                center=(text_center_x, 475),
            )

        draw_text(
            surface,
            self.app.translate(Text.RESULTS_REPLAY),
            self.text_font,
            THEME.text_secondary,
            center=(center_x, 585),
        )

        draw_text(
            surface,
            self.app.translate(Text.RESULTS_BACK_TO_TITLE),
            self.text_font,
            THEME.text_muted,
            center=(center_x, 670),
        )
