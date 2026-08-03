import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FRAMES_PER_SECOND = 60

BACKGROUND_COLOR = (14, 20, 36)
TITLE_COLOR = (245, 247, 255)
SUBTITLE_COLOR = (151, 163, 184)


class PygameApp:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Beat the Maths")

        self.clock = pygame.time.Clock()
        self.running = True

        self.title_font = pygame.font.Font(None, 88)
        self.subtitle_font = pygame.font.Font(None, 36)

    def run(self) -> None:
        try:
            while self.running:
                delta_time = self.clock.tick(FRAMES_PER_SECOND) / 1000
                self.handle_events()
                self.update(delta_time)
                self.draw()
        finally:
            pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)

        title = self.title_font.render(
            "BEAT THE MATHS",
            True,
            TITLE_COLOR,
        )
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30))
        self.screen.blit(title, title_rect)

        subtitle = self.subtitle_font.render(
            "The serious game to heal your maths pain.",
            True,
            SUBTITLE_COLOR,
        )
        subtitle_rect = subtitle.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 45)
        )
        self.screen.blit(subtitle, subtitle_rect)

        pygame.display.flip()


def main() -> None:
    app = PygameApp()
    app.run()
