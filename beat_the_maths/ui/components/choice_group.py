import pygame

from .button import Button


class ChoiceGroup[T]:
    def __init__(self, buttons: dict[T, Button]) -> None:
        self._buttons = buttons
        self.selected: T | None = None

    def handle_event(self, event: pygame.event.Event) -> bool:
        for value, button in self._buttons.items():
            if button.handle_event(event):
                self.selected = value
                return True

        return False

    def draw(self, surface: pygame.Surface) -> None:
        for value, button in self._buttons.items():
            button.draw(
                surface,
                selected=value == self.selected,
            )
