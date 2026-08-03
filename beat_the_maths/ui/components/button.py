import pygame

DEFAULT_COLOR = (30, 41, 59)
HOVER_COLOR = (45, 65, 95)
SELECTED_COLOR = (37, 99, 235)

DEFAULT_BORDER_COLOR = (71, 85, 105)
HOVER_BORDER_COLOR = (96, 165, 250)
SELECTED_BORDER_COLOR = (147, 197, 253)

TEXT_COLOR = (241, 245, 249)


class Button:
    def __init__(
        self,
        text: str,
        rect: tuple[int, int, int, int],
        font: pygame.font.Font,
    ) -> None:
        self.text = text
        self.rect = pygame.Rect(rect)
        self.font = font

    def handle_event(self, event: pygame.event.Event) -> bool:
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

    def draw(
        self,
        surface: pygame.Surface,
        selected: bool = False,
    ) -> None:
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())

        if selected:
            background_color = SELECTED_COLOR
            border_color = SELECTED_BORDER_COLOR
        elif hovered:
            background_color = HOVER_COLOR
            border_color = HOVER_BORDER_COLOR
        else:
            background_color = DEFAULT_COLOR
            border_color = DEFAULT_BORDER_COLOR

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

        rendered_text = self.font.render(
            self.text,
            True,
            TEXT_COLOR,
        )

        text_rect = rendered_text.get_rect(center=self.rect.center)

        surface.blit(rendered_text, text_rect)
