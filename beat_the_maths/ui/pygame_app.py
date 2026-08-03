import pygame

from .scenes.scene import Scene
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

    def change_scene(self, scene: Scene) -> None:
        self.scene = scene


def main() -> None:
    app = PygameApp()
    app.run()
