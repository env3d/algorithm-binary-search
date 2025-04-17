import pygame
import random
import bisect
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUILDING_WIDTH = 20
BUILDING_HEIGHT = 200
NUM_BUILDINGS = 1000000
VISIBLE_RANGE = 400
PLAYER_SPEED = 5

# Modes
USE_BINARY_SEARCH = False

# Character properties
CHARACTER_WIDTH = 20
CHARACTER_HEIGHT = 40
CHARACTER_COLOR = (255, 255, 0)  # Yellow
character_y = SCREEN_HEIGHT - CHARACTER_HEIGHT  # Position at the bottom of the screen

# Setup Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# Generate buildings with sorted x-positions, random heights, and colors
building_positions = sorted(random.randint(0, NUM_BUILDINGS * BUILDING_WIDTH) for _ in range(NUM_BUILDINGS))
building_heights = [random.randint(100, BUILDING_HEIGHT) for _ in range(NUM_BUILDINGS)]
building_colors = [(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for _ in range(NUM_BUILDINGS)]

# Game State
player_x = SCREEN_WIDTH // 2

# Binary search helper
def get_visible_buildings_binary(player_pos):
    left = player_pos - VISIBLE_RANGE
    right = player_pos + VISIBLE_RANGE
    i = bisect.bisect_left(building_positions, left)
    j = bisect.bisect_right(building_positions, right)
    return building_positions[i:j]

# Linear search helper
def get_visible_buildings_linear(player_pos):
    left = player_pos - VISIBLE_RANGE
    right = player_pos + VISIBLE_RANGE
    return [x for x in building_positions if left <= x <= right]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                USE_BINARY_SEARCH = not USE_BINARY_SEARCH

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED

    # Clear screen
    screen.fill((30, 30, 30))

    # Get visible buildings
    start_time = time.perf_counter()
    if USE_BINARY_SEARCH:
        visible_buildings = get_visible_buildings_binary(player_x)
    else:
        visible_buildings = get_visible_buildings_linear(player_x)
    search_time = (time.perf_counter() - start_time) * 1000  # ms

    # Draw buildings
    for i, x in enumerate(visible_buildings):
        screen_x = x - player_x + SCREEN_WIDTH // 2
        building_index = building_positions.index(x)  # Get the index of the building
        height = building_heights[building_index]
        color = building_colors[building_index]
        pygame.draw.rect(screen, color, (screen_x, SCREEN_HEIGHT - height, BUILDING_WIDTH, height))

    # Draw character
    pygame.draw.rect(screen, CHARACTER_COLOR, (SCREEN_WIDTH // 2 - CHARACTER_WIDTH // 2, character_y, CHARACTER_WIDTH, CHARACTER_HEIGHT))

    # Draw info
    mode_text = f"Mode: {'Binary Search' if USE_BINARY_SEARCH else 'Linear Search'}"
    fps_text = f"FPS: {clock.get_fps():.1f}"
    time_text = f"Search Time: {search_time:.2f} ms"
    screen.blit(font.render(mode_text, True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(fps_text, True, (255, 255, 255)), (10, 30))
    screen.blit(font.render(time_text, True, (255, 255, 255)), (10, 50))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
