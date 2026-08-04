from typing import TYPE_CHECKING

import pygame

from ...i18n import Language, Text
from ..components.button import Button
from ..components.choice_group import ChoiceGroup
from ..drawing import draw_text
from ..layout import centered_row
from ..theme import THEME, get_font
from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp


class SettingsScene(Scene):
    def __init__(self, app: "PygameApp") -> None:
        super().__init__(app)

        self.title_font = get_font(68)
        self.section_font = get_font(42)
        self.button_font = get_font(34)
        self.help_font = get_font(28)

        center_x = self.app.screen.get_rect().centerx

        language_options = [
            (Language.FRENCH, "Français"),
            (Language.ENGLISH, "English"),
        ]

        language_rects = centered_row(
            len(language_options),
            center_x=center_x,
            top=290,
            item_size=(300, 64),
            gap=30,
        )

        self.language_group = ChoiceGroup(
            {
                language: Button(label, rect, self.button_font)
                for (language, label), rect in zip(
                    language_options, language_rects, strict=True
                )
            }
        )
        self.language_group.selected = self.app.settings.language

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            self.app.show_title()
            return

        if self.language_group.handle_event(event):
            language = self.language_group.selected
            assert language is not None

            self.app.set_language(language)

    def draw_content(self, surface: pygame.Surface) -> None:
        center_x = surface.get_rect().centerx

        draw_text(
            surface,
            self.app.translate(Text.SETTINGS_TITLE),
            self.title_font,
            THEME.heading,
            center=(center_x, 110),
        )

        draw_text(
            surface,
            self.app.translate(Text.SETTINGS_LANGUAGE),
            self.section_font,
            THEME.accent,
            center=(center_x, 230),
        )

        self.language_group.draw(surface)

        draw_text(
            surface,
            self.app.translate(Text.SETTINGS_BACK),
            self.help_font,
            THEME.text_muted,
            center=(center_x, 660),
        )
