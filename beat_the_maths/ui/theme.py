from dataclasses import dataclass
from functools import cache

import pygame

type Color = tuple[int, int, int]


@dataclass(frozen=True)
class Theme:
    background: Color = (14, 20, 36)

    heading: Color = (245, 247, 255)
    text_primary: Color = (241, 245, 249)
    text_secondary: Color = (203, 213, 225)
    text_subtitle: Color = (151, 163, 184)
    text_muted: Color = (120, 132, 153)
    text_disabled: Color = (100, 116, 139)

    accent: Color = (88, 166, 255)
    success: Color = (74, 222, 128)
    failure: Color = (248, 113, 113)

    surface: Color = (30, 41, 59)
    surface_hover: Color = (45, 65, 95)
    surface_selected: Color = (37, 99, 235)
    surface_disabled: Color = (25, 32, 45)
    input_background: Color = (15, 23, 42)

    border: Color = (71, 85, 105)
    border_hover: Color = (96, 165, 250)
    border_selected: Color = (147, 197, 253)
    border_disabled: Color = (51, 65, 85)


THEME = Theme()


@cache
def get_font(size: int) -> pygame.font.Font:
    return pygame.font.Font(None, size)
