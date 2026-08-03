import math
from typing import TYPE_CHECKING

import pygame

from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
SUBTITLE_COLOR = (151, 163, 184)
ACTION_COLOR = (88, 166, 255)


class TitleScene(Scene):
    def __init__(self, app: "PygameApp") -> None:
        super().__init__(app)

        self.title_font = pygame.font.Font(None, 88)
        self.subtitle_font = pygame.font.Font(None, 36)
        self.action_font = pygame.font.Font(None, 42)

        self.elapsed_time = 0.0

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            from .configuration_scene import ConfigurationScene

            self.app.change_scene(ConfigurationScene(self.app))

    def update(self, delta_time: float) -> None:
        self.elapsed_time += delta_time

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
            center=(center_x, center_y - 100),
        )
        surface.blit(title, title_rect)

        subtitle = self.subtitle_font.render(
            "The serious game to heal your maths pain.",
            True,
            SUBTITLE_COLOR,
        )
        subtitle_rect = subtitle.get_rect(
            center=(center_x, center_y - 25),
        )
        surface.blit(subtitle, subtitle_rect)

        pulse = (math.sin(self.elapsed_time * 3) + 1) / 2
        alpha = int(120 + pulse * 135)

        action = self.action_font.render(
            "Appuie sur Entrée pour jouer",
            True,
            ACTION_COLOR,
        )
        action.set_alpha(alpha)

        action_rect = action.get_rect(
            center=(center_x, center_y + 100),
        )
        surface.blit(action, action_rect)
