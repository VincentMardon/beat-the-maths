from typing import TYPE_CHECKING

import pygame

from ...core.services.quiz_engine.quiz_config import (
    Difficulty,
    Operation,
    QuizConfig,
)
from ...i18n import Text
from ..components.button import Button
from ..components.choice_group import ChoiceGroup
from ..components.text_input import TextInput
from ..drawing import draw_text
from ..layout import centered_row
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

        center_x = self.app.screen.get_rect().centerx

        operation_options = [
            (Operation.ADDITION, self.app.translate(Text.OPERATION_ADDITION)),
            (Operation.SUBTRACTION, self.app.translate(Text.OPERATION_SUBTRACTION)),
            (
                Operation.MULTIPLICATION,
                self.app.translate(Text.OPERATION_MULTIPLICATION),
            ),
            (Operation.DIVISION, self.app.translate(Text.OPERATION_DIVISION)),
        ]

        operation_rects = centered_row(
            len(operation_options),
            center_x=center_x,
            top=145,
            item_size=(240, 56),
            gap=20,
        )

        self.operation_group = ChoiceGroup(
            {
                operation: Button(label, rect, self.button_font)
                for (operation, label), rect in zip(
                    operation_options, operation_rects, strict=True
                )
            }
        )

        difficulty_options = [
            (Difficulty.EASY, self.app.translate(Text.DIFFICULTY_EASY)),
            (Difficulty.MEDIUM, self.app.translate(Text.DIFFICULTY_MEDIUM)),
            (Difficulty.HARD, self.app.translate(Text.DIFFICULTY_HARD)),
        ]

        difficulty_rects = centered_row(
            len(difficulty_options),
            center_x=center_x,
            top=265,
            item_size=(240, 56),
            gap=30,
        )

        self.difficulty_group = ChoiceGroup(
            {
                difficulty: Button(label, rect, self.button_font)
                for (difficulty, label), rect in zip(
                    difficulty_options,
                    difficulty_rects,
                    strict=True,
                )
            }
        )

        question_count_rects = centered_row(
            5,
            center_x=center_x,
            top=385,
            item_size=(160, 58),
            gap=16,
        )

        self.question_count_group = ChoiceGroup(
            {
                question_count: Button(
                    str(question_count),
                    rect,
                    self.button_font,
                )
                for question_count, rect in zip(
                    (5, 10, 20, 50),
                    question_count_rects[:4],
                    strict=True,
                )
            }
        )
        self.question_count_group.selected = 10

        self.question_count_input = TextInput(
            rect=question_count_rects[4],
            font=self.button_font,
            placeholder=self.app.translate(Text.QUESTION_COUNT_CUSTOM),
            maximum_length=None,
        )

        self.start_button = Button(
            self.app.translate(Text.START),
            (480, 520, 320, 64),
            self.button_font,
            enabled=False,
        )

    def _selected_question_count(self) -> int | None:
        if self.question_count_input.text:
            question_count = int(self.question_count_input.text)

            if question_count > 0:
                return question_count

            return None

        return self.question_count_group.selected

    def handle_event(self, event: pygame.event.Event) -> None:
        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_BACKSPACE
            and not self.question_count_input.text
        ):
            self.app.show_title()
            return

        if self.operation_group.handle_event(event):
            return

        if self.difficulty_group.handle_event(event):
            return

        if self.question_count_group.handle_event(event):
            self.question_count_input.clear()
            return

        previous_text = self.question_count_input.text
        self.question_count_input.handle_event(event)

        if self.question_count_input.text != previous_text:
            self.question_count_group.selected = None
            return

        if self.start_button.handle_event(event):
            operation = self.operation_group.selected
            difficulty = self.difficulty_group.selected
            question_count = self._selected_question_count()

            assert operation is not None
            assert difficulty is not None
            assert question_count is not None

            config = QuizConfig(
                difficulty=difficulty,
                operation=operation,
                question_count=question_count,
            )

            self.app.start_quiz(config)

    def update(self, _delta_time: float) -> None:
        self.start_button.enabled = (
            self.operation_group.selected is not None
            and self.difficulty_group.selected is not None
            and self._selected_question_count() is not None
        )

    def draw_content(self, surface: pygame.Surface) -> None:
        center_x = surface.get_rect().centerx

        draw_text(
            surface,
            self.app.translate(Text.CONFIGURATION_TITLE),
            self.title_font,
            THEME.heading,
            center=(center_x, 50),
        )

        draw_text(
            surface,
            self.app.translate(Text.OPERATION_PROMPT),
            self.section_font,
            THEME.accent,
            center=(center_x, 115),
        )

        self.operation_group.draw(surface)

        draw_text(
            surface,
            self.app.translate(Text.DIFFICULTY_PROMPT),
            self.section_font,
            THEME.accent,
            center=(center_x, 235),
        )

        self.difficulty_group.draw(surface)

        draw_text(
            surface,
            self.app.translate(Text.QUESTION_COUNT_PROMPT),
            self.section_font,
            THEME.accent,
            center=(center_x, 355),
        )

        self.question_count_group.draw(surface)
        self.question_count_input.draw(surface)

        question_count = self._selected_question_count()

        if self.question_count_input.text and question_count is None:
            help_text = self.app.translate(Text.QUESTION_COUNT_INVALID)
        elif (
            self.operation_group.selected is not None
            and self.difficulty_group.selected is not None
            and question_count is not None
        ):
            help_text = self.app.translate(Text.CONFIGURATION_READY)
        else:
            help_text = self.app.translate(Text.CONFIGURATION_INCOMPLETE)

        draw_text(
            surface,
            help_text,
            self.help_font,
            THEME.text_muted,
            center=(center_x, 490),
        )

        self.start_button.draw(surface)

        draw_text(
            surface,
            self.app.translate(Text.BACK_TO_TITLE),
            self.help_font,
            THEME.text_muted,
            center=(center_x, 660),
        )
