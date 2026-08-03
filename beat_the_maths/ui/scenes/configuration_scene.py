from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.quiz_config import Difficulty, Operation
from ..components.button import Button
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
SECTION_COLOR = (88, 166, 255)
HELP_COLOR = (120, 132, 153)


class ConfigurationScene(Scene):
    def __init__(self, app: "PygameApp") -> None:
        super().__init__(app)

        self.title_font = pygame.font.Font(None, 68)
        self.section_font = pygame.font.Font(None, 42)
        self.button_font = pygame.font.Font(None, 34)
        self.help_font = pygame.font.Font(None, 28)

        self.selected_operation: Operation | None = None
        self.selected_difficulty: Difficulty | None = None

        self.operation_buttons = {
            Operation.ADDITION: Button(
                "Addition", (130, 220, 240, 64), self.button_font
            ),
            Operation.SUBTRACTION: Button(
                "Soustraction", (390, 220, 240, 64), self.button_font
            ),
            Operation.MULTIPLICATION: Button(
                "Multiplication", (650, 220, 240, 64), self.button_font
            ),
            Operation.DIVISION: Button(
                "Division", (910, 220, 240, 64), self.button_font
            ),
        }

        self.difficulty_buttons = {
            Difficulty.EASY: Button(
                "Facile",
                (250, 420, 240, 64),
                self.button_font,
            ),
            Difficulty.MEDIUM: Button(
                "Moyenne",
                (520, 420, 240, 64),
                self.button_font,
            ),
            Difficulty.HARD: Button(
                "Difficile",
                (790, 420, 240, 64),
                self.button_font,
            ),
        }

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            from .title_scene import TitleScene

            self.app.change_scene(TitleScene(self.app))
            return

        for operation, button in self.operation_buttons.items():
            if button.handle_event(event):
                self.selected_operation = operation
                return

        for difficulty, button in self.difficulty_buttons.items():
            if button.handle_event(event):
                self.selected_difficulty = difficulty
                return

    def update(self, _delta_time: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(BACKGROUND_COLOR)

        center_x = surface.get_rect().centerx

        self._draw_centered_text(
            surface,
            "CONFIGURE TA PARTIE",
            self.title_font,
            TITLE_COLOR,
            center_x,
            75,
        )

        self._draw_centered_text(
            surface,
            "Choisis une opération",
            self.section_font,
            SECTION_COLOR,
            center_x,
            165,
        )

        for operation, button in self.operation_buttons.items():
            button.draw(
                surface,
                selected=operation is self.selected_operation,
            )

        self._draw_centered_text(
            surface,
            "Choisis une difficulté",
            self.section_font,
            SECTION_COLOR,
            center_x,
            365,
        )

        for difficulty, button in self.difficulty_buttons.items():
            button.draw(surface, selected=difficulty is self.selected_difficulty)

        if self.selected_operation is not None and self.selected_difficulty is not None:
            help_text = "Configuration prête !"
        else:
            help_text = "Sélectionne une opération et une difficulté"

        self._draw_centered_text(
            surface,
            help_text,
            self.help_font,
            HELP_COLOR,
            center_x,
            570,
        )

        self._draw_centered_text(
            surface,
            "Retour arrière : revenir au titre    •    Échap : quitter",
            self.help_font,
            HELP_COLOR,
            center_x,
            660,
        )

    @staticmethod
    def _draw_centered_text(
        surface: pygame.Surface,
        text: str,
        font: pygame.font.Font,
        color: tuple[int, int, int],
        center_x: int,
        center_y: int,
    ) -> None:
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect(center=(center_x, center_y))
        surface.blit(rendered_text, text_rect)
