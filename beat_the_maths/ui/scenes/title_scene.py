import math
from typing import TYPE_CHECKING

import pygame

from ..drawing import draw_text
from ..theme import THEME, get_font
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp


class TitleScene(Scene):
    def __init__(self, app: "PygameApp") -> None:
        super().__init__(app)

        self.title_font = get_font(88)
        self.subtitle_font = get_font(36)
        self.action_font = get_font(42)

        self.elapsed_time = 0.0

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.app.show_configuration()

    def update(self, delta_time: float) -> None:
        self.elapsed_time += delta_time

    def draw_content(self, surface: pygame.Surface) -> None:
        center_x = surface.get_rect().centerx
        center_y = surface.get_rect().centery

        draw_text(
            surface,
            "BEAT THE MATHS",
            self.title_font,
            THEME.heading,
            center=(center_x, center_y - 100),
        )

        draw_text(
            surface,
            "The serious game to heal your maths pain.",
            self.subtitle_font,
            THEME.text_subtitle,
            center=(center_x, center_y - 25),
        )

        pulse = (math.sin(self.elapsed_time * 3) + 1) / 2
        alpha = int(120 + pulse * 135)

        draw_text(
            surface,
            "Appuie sur Entrée pour jouer",
            self.action_font,
            THEME.accent,
            center=(center_x, center_y + 100),
            alpha=alpha,
        )
