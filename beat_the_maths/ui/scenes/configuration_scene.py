from typing import TYPE_CHECKING

import pygame

from .scene import Scene

if TYPE_CHECKING:
    from ..pygame_app import PygameApp

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
SECTION_COLOR = (88, 166, 255)
TEXT_COLOR = (203, 213, 225)
HELP_COLOR = (120, 132, 153)


class ConfigurationScene(Scene):
    def __init__(self, app: "PygameApp") -> None:
        super().__init__(app)

        self.title_font = pygame.font.Font(None, 68)
        self.section_font = pygame.font.Font(None, 42)
        self.text_font = pygame.font.Font(None, 34)
        self.help_font = pygame.font.Font(None, 28)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            from .title_scene import TitleScene

            self.app.change_scene(TitleScene(self.app))

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
            90,
        )

        self._draw_centered_text(
            surface,
            "Opération",
            self.section_font,
            SECTION_COLOR,
            center_x,
            210,
        )

        self._draw_centered_text(
            surface,
            "Addition  •  Soustraction  •  Multiplication  •  Division",
            self.text_font,
            TEXT_COLOR,
            center_x,
            265,
        )

        self._draw_centered_text(
            surface,
            "Difficulté",
            self.section_font,
            SECTION_COLOR,
            center_x,
            390,
        )

        self._draw_centered_text(
            surface,
            "Facile  •  Moyenne  •  Difficile",
            self.text_font,
            TEXT_COLOR,
            center_x,
            445,
        )

        self._draw_centered_text(
            surface,
            "Retour arrière : revenir au titre    •    Échap : quitter",
            self.help_font,
            HELP_COLOR,
            center_x,
            650,
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
