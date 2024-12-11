import pygame

# Setup global constants
FRAME_REFRESH_RATE = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400


class Game:
    """Represents the game itself, holds the main game playing loop"""
    def __init__(self):
        print('Initializing PyGame')
        pygame.init()
        # Set up the display
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption('Starship Meteors')
        # Used for timing within the program
        self.clock = pygame.time.Clock()

    def play(self):
        is_running = True

        # Main game Playing Loop
        while is_running:
            # Work out what the user wants to do
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    # Check to see which key is pressed
                    if event.key == pygame.K_q:
                        is_running = False

            # Update the display
            pygame.display.update()

            # Defines the frame rate. The number is number of frames per second
            # Should be called once per frame (but only once)
            self.clock.tick(FRAME_REFRESH_RATE)

        # Let pygame shutdown gracefully
        pygame.quit()


def main():
    print('Starting Game')
    game = Game()
    game.play()
    print('Game Over')

if __name__ == '__main__':
    main()