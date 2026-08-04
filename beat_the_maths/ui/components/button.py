import pygame

from ..drawing import draw_text
from ..theme import THEME


class Button:
    def __init__(
        self,
        text: str,
        rect: tuple[int, int, int, int],
        font: pygame.font.Font,
        enabled: bool = True,
    ) -> None:
        self.text = text
        self.rect = pygame.Rect(rect)
        self.font = font
        self.enabled = enabled

    def handle_event(self, event: pygame.event.Event) -> bool:
        return (
            self.enabled
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

    def draw(
        self,
        surface: pygame.Surface,
        selected: bool = False,
    ) -> None:
        hovered = self.enabled and self.rect.collidepoint(pygame.mouse.get_pos())

        if not self.enabled:
            background_color = THEME.surface_disabled
            border_color = THEME.border_disabled
            text_color = THEME.text_disabled
        elif selected:
            background_color = THEME.surface_selected
            border_color = THEME.border_selected
            text_color = THEME.text_primary
        elif hovered:
            background_color = THEME.surface_hover
            border_color = THEME.border_hover
            text_color = THEME.text_primary
        else:
            background_color = THEME.surface
            border_color = THEME.border
            text_color = THEME.text_primary

        pygame.draw.rect(
            surface,
            background_color,
            self.rect,
            border_radius=14,
        )

        pygame.draw.rect(
            surface,
            border_color,
            self.rect,
            width=2,
            border_radius=14,
        )

        draw_text(
            surface,
            self.text,
            self.font,
            text_color,
            center=self.rect.center,
        )
