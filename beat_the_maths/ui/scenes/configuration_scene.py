from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
    QuizConfig,
)
from ..components.button import Button
from ..drawing import draw_text
from ..theme import THEME, get_font
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp


class ConfigurationScene(Scene):
    def __init__(self, app: "PygameApp") -> None:
        super().__init__(app)

        self.title_font = get_font(68)
        self.section_font = get_font(42)
        self.button_font = get_font(34)
        self.help_font = get_font(28)

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

        self.start_button = Button(
            "Commencer",
            (480, 550, 320, 64),
            self.button_font,
            enabled=False,
        )

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

        if self.start_button.handle_event(event):
            assert self.selected_operation is not None
            assert self.selected_difficulty is not None

            from .quiz_scene import QuizScene

            config = QuizConfig(
                difficulty=self.selected_difficulty, operation=self.selected_operation
            )

            self.app.change_scene(
                QuizScene(
                    app=self.app,
                    config=config,
                )
            )

    def update(self, _delta_time: float) -> None:
        self.start_button.enabled = (
            self.selected_operation is not None and self.selected_difficulty is not None
        )

    def draw_content(self, surface: pygame.Surface) -> None:
        center_x = surface.get_rect().centerx

        draw_text(
            surface,
            "CONFIGURE TA PARTIE",
            self.title_font,
            THEME.heading,
            center=(center_x, 75),
        )

        draw_text(
            surface,
            "Choisis une opération",
            self.section_font,
            THEME.accent,
            center=(center_x, 165),
        )

        for operation, button in self.operation_buttons.items():
            button.draw(
                surface,
                selected=operation is self.selected_operation,
            )

        draw_text(
            surface,
            "Choisis une difficulté",
            self.section_font,
            THEME.accent,
            center=(center_x, 365),
        )

        for difficulty, button in self.difficulty_buttons.items():
            button.draw(surface, selected=difficulty is self.selected_difficulty)

        if self.selected_operation is not None and self.selected_difficulty is not None:
            help_text = "Configuration prête !"
        else:
            help_text = "Sélectionne une opération et une difficulté"

        draw_text(
            surface,
            help_text,
            self.help_font,
            THEME.text_muted,
            center=(center_x, 515),
        )

        self.start_button.draw(surface)

        draw_text(
            surface,
            "Retour arrière : revenir au titre    •    Échap : quitter",
            self.help_font,
            THEME.text_muted,
            center=(center_x, 660),
        )
