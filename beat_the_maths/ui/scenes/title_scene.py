from typing import TYPE_CHECKING

import pygame

from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
SUBTITLE_COLOR = (151, 163, 184)


class TitleScene(Scene):
    def __init__(self, app: "PygameApp") -> None:
        super().__init__(app)

        self.title_font = pygame.font.Font(None, 88)
        self.subtitle_font = pygame.font.Font(None, 36)

    def handle_event(self, _event: pygame.event.Event) -> None:
        pass

    def update(self, _delta_time: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(BACKGROUND_COLOR)

        center_x = surface.get_rect().centerx
        center_y = surface.get_rect().centery

        title = self.title_font.render(
            "BEAT THE MATHS",
            True,
            TITLE_COLOR,
        )
        title_rect = title.get_rect(
            center=(center_x, center_y - 30),
        )
        surface.blit(title, title_rect)

        subtitle = self.subtitle_font.render(
            "The serious game to heal your maths pain.",
            True,
            SUBTITLE_COLOR,
        )
        subtitle_rect = subtitle.get_rect(
            center=(center_x, center_y + 45),
        )
        surface.blit(subtitle, subtitle_rect)
