from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import pygame

from ..theme import THEME

if TYPE_CHECKING:
    from ..pygame_app import PygameApp


class Scene(ABC):
    def __init__(self, app: "PygameApp") -> None:
        self.app = app

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta_time: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(THEME.background)
        self.draw_content(surface)

    @abstractmethod
    def draw_content(self, surface: pygame.Surface) -> None:
        pass
