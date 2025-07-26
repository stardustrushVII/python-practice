import pygame
import sys

def main():
    # initial setup
    pygame.init()
    SCREEN_WIDTH = 1910
    SCREEN_HEIGHT = 1080
    LEVEL_WIDTH = 2000
    start_ticks = pygame.time.get_ticks()  # millisecs since initialisation


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Most Boring Racing Game Ever")
    clock = pygame.time.Clock()

    # (Sonic) Colours
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    PURPLE = (128, 0, 128)

    # players
    PLAYER_RADIUS = 15
    player1_pos = [100, 300]
    player2_pos = [100, 360]
    player_speed = 5

    finish_x = LEVEL_WIDTH - 100
    font = pygame.font.SysFont(None, 48)

    running = True
    winner = None

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if winner and event.key == pygame.K_r:
                    main()  # r
                    return

        keys = pygame.key.get_pressed()

        

        if winner is None:
            if keys[pygame.K_a]:
                player1_pos[0] -= player_speed
            if keys[pygame.K_d]:
                player1_pos[0] += player_speed
            if keys[pygame.K_LEFT]:
                player2_pos[0] -= player_speed
            if keys[pygame.K_RIGHT]:
                player2_pos[0] += player_speed

            player1_pos[0] = max(0, min(player1_pos[0], LEVEL_WIDTH))
            player2_pos[0] = max(0, min(player2_pos[0], LEVEL_WIDTH))

            if player1_pos[0] >= finish_x:
                winner = "Player 1"
            elif player2_pos[0] >= finish_x:
                winner = "Player 2"

                

        # track draw
        pygame.draw.rect(screen, BLACK, (0, 380, LEVEL_WIDTH, 20))
        pygame.draw.rect(screen, GREEN, (finish_x, 0, 10, SCREEN_HEIGHT))
        pygame.draw.circle(screen, RED,  (player1_pos[0], player1_pos[1]), PLAYER_RADIUS)
        pygame.draw.circle(screen, BLUE, (player2_pos[0], player2_pos[1]), PLAYER_RADIUS)

        if winner:
            text = font.render(f"{winner} Wins! You Get Nothing!", True, (0, 0, 0))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 30))
            restart_text = font.render("Press R to restart", True, (0, 0, 0))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 80))

        pygame.display.flip()
        clock.tick(60)

# exe (or .app)
main()
pygame.quit()
sys.exit()
