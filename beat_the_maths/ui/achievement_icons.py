from functools import cache
from importlib import resources

import pygame

from ..core.user_profile import AchievementId
from .theme import THEME, get_font

ACHIEVEMENT_ICON_SIZE = (128, 128)


@cache
def load_achievement_icon(
    achievement_id: AchievementId,
    size: tuple[int, int] = ACHIEVEMENT_ICON_SIZE,
) -> pygame.Surface:
    resource = resources.files("beat_the_maths").joinpath(
        "assets", "badges", f"{achievement_id.value}.png"
    )

    try:
        with resources.as_file(resource) as resource_path:
            image = pygame.image.load(resource_path).convert_alpha()
    except (FileNotFoundError, pygame.error):
        return _create_placeholder(size)

    return pygame.transform.smoothscale(image, size)


def _create_placeholder(size: tuple[int, int]) -> pygame.Surface:
    placeholder = pygame.Surface(size, pygame.SRCALPHA)
    rect = placeholder.get_rect()

    pygame.draw.rect(
        placeholder,
        THEME.surface_hover,
        rect,
        border_radius=20,
    )
    pygame.draw.rect(
        placeholder,
        THEME.border_selected,
        rect,
        width=3,
        border_radius=20,
    )

    question_mark = get_font(90).render(
        "?",
        True,
        THEME.text_muted,
    )
    placeholder.blit(
        question_mark,
        question_mark.get_rect(center=rect.center),
    )

    return placeholder
