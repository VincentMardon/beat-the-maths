import pygame

from ..core.services.achievement_engine import unlock_achievements
from ..core.services.quiz_engine.game_session import GameSession
from ..core.services.quiz_engine.quiz_config import QuizConfig
from ..core.user_profile import UserProfile
from ..i18n import Language, Text
from ..i18n import translate as translate_text
from .app_settings import AppSettings
from .scenes.configuration_scene import ConfigurationScene
from .scenes.quiz_scene import QuizScene
from .scenes.results_scene import ResultsScene
from .scenes.scene import Scene
from .scenes.settings_scene import SettingsScene
from .scenes.title_scene import TitleScene

WINDOW_SIZE = (1280, 720)
FRAMES_PER_SECOND = 60


class PygameApp:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Beat the Maths")

        self.clock = pygame.time.Clock()
        self.running = True
        self.settings = AppSettings()
        self.profile = UserProfile()
        self.scene: Scene = TitleScene(self)

    def run(self) -> None:
        try:
            while self.running:
                delta_time = self.clock.tick(FRAMES_PER_SECOND) / 1000

                self.handle_events()
                self.scene.update(delta_time)
                self.draw()
        finally:
            pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            else:
                self.scene.handle_event(event)

    def draw(self) -> None:
        self.scene.draw(self.screen)
        pygame.display.flip()

    def show_title(self) -> None:
        self._change_scene(TitleScene(self))

    def show_configuration(self) -> None:
        self._change_scene(ConfigurationScene(self))

    def show_settings(self) -> None:
        self._change_scene(SettingsScene(self))

    def start_quiz(self, config: QuizConfig) -> None:
        self._change_scene(
            QuizScene(
                app=self,
                config=config,
            )
        )

    def show_results(self, session: GameSession) -> None:
        newly_unlocked = unlock_achievements(
            self.profile,
            session,
        )

        self._change_scene(
            ResultsScene(app=self, session=session, newly_unlocked=newly_unlocked)
        )

    def _change_scene(self, scene: Scene) -> None:
        self.scene = scene

    def set_language(self, language: Language) -> None:
        self.settings.language = language

    def translate(self, text: Text, **values: object) -> str:
        return translate_text(
            self.settings.language,
            text,
            **values,
        )


def main() -> None:
    app = PygameApp()
    app.run()
