import pygame

from ..drawing import draw_text
from ..theme import THEME


class TextInput:
    def __init__(
        self,
        rect: tuple[int, int, int, int],
        font: pygame.font.Font,
        placeholder: str = "",
        maximum_length: int | None = 12,
    ) -> None:
        self.rect = pygame.Rect(rect)
        self.font = font
        self.placeholder = placeholder
        self.maximum_length = maximum_length
        self.text = ""
        self.enabled = True

    def handle_event(self, event: pygame.event.Event) -> bool:
        if not self.enabled or event.type != pygame.KEYDOWN:
            return False

        if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            return bool(self.text)

        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif event.unicode.isdigit() and (
            self.maximum_length is None or len(self.text) < self.maximum_length
        ):
            self.text += event.unicode

        return False

    def clear(self) -> None:
        self.text = ""

    def draw(self, surface: pygame.Surface) -> None:
        border_color = THEME.border_hover if self.enabled else THEME.border

        pygame.draw.rect(
            surface,
            THEME.input_background,
            self.rect,
            border_radius=14,
        )

        pygame.draw.rect(
            surface,
            border_color,
            self.rect,
            width=3,
            border_radius=14,
        )

        if self.text:
            displayed_text = self.text
            text_color = THEME.text_primary
        else:
            displayed_text = self.placeholder
            text_color = THEME.text_disabled

        draw_text(
            surface,
            displayed_text,
            self.font,
            text_color,
            center=self.rect.center,
        )
