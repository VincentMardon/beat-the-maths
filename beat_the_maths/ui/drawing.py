import pygame

from .theme import Color


def draw_text(
    surface: pygame.Surface,
    text: str,
    font: pygame.font.Font,
    color: Color,
    *,
    center: tuple[int, int],
    alpha: int | None = None,
) -> pygame.Rect:
    rendered_text = font.render(text, True, color)

    if alpha is not None:
        rendered_text.set_alpha(alpha)

    text_rect = rendered_text.get_rect(center=center)
    surface.blit(rendered_text, text_rect)

    return text_rect
