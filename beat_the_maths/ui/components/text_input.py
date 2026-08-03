import pygame

BACKGROUND_COLOR = (15, 23, 42)
ACTIVE_BORDER_COLOR = (96, 165, 250)
DISABLED_BORDER_COLOR = (71, 85, 105)
TEXT_COLOR = (241, 245, 249)
PLACEHOLDER_COLOR = (100, 116, 139)


class TextInput:
    def __init__(
        self,
        rect: tuple[int, int, int, int],
        font: pygame.font.Font,
        placeholder: str = "",
        maximum_length: int = 12,
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
        elif event.unicode.isdigit() and len(self.text) < self.maximum_length:
            self.text += event.unicode

        return False

    def clear(self) -> None:
        self.text = ""

    def draw(self, surface: pygame.Surface) -> None:
        border_color = ACTIVE_BORDER_COLOR if self.enabled else DISABLED_BORDER_COLOR

        pygame.draw.rect(
            surface,
            BACKGROUND_COLOR,
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
            text_color = TEXT_COLOR
        else:
            displayed_text = self.placeholder
            text_color = PLACEHOLDER_COLOR

        rendered_text = self.font.render(
            displayed_text,
            True,
            text_color,
        )

        text_rect = rendered_text.get_rect(
            center=self.rect.center,
        )

        surface.blit(rendered_text, text_rect)
