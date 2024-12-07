import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
block_size = 30
cols = width // block_size
rows = height // block_size

# Colors
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]

# Tetrimino shapes
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Initialize the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Tetris Game")

# Draw grid
def draw_grid():
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen, (200, 200, 200), (x * block_size, y * block_size, block_size, block_size), 1)

# Check if the position is valid
def valid_position(grid, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell and (grid[y + off_y][x + off_x] or y + off_y >= len(grid) or x + off_x >= len(grid[0])):
                return False
    return True

# Merge shape into the grid
def merge_shape(grid, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + off_y][x + off_x] = cell

# Clear completed lines
def clear_lines(grid):
    full_rows = [i for i, row in enumerate(grid) if all(row)]
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0 for _ in range(cols)])
    return len(full_rows)

# Main game loop
def game():
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    current_shape = random.choice(shapes)
    shape_pos = [0, cols // 2 - len(current_shape[0]) // 2]
    clock = pygame.time.Clock()
    fall_time = 0

    while True:
        screen.fill((0, 0, 0))
        fall_speed = 0.5
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            shape_pos[0] += 1
            if not valid_position(grid, current_shape, shape_pos):
                shape_pos[0] -= 1
                merge_shape(grid, current_shape, shape_pos)
                current_shape = random.choice(shapes)
                shape_pos = [0, cols // 2 - len(current_shape[0]) // 2]
                if not valid_position(grid, current_shape, shape_pos):
                    break  # Game over

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shape_pos[1] -= 1
                    if not valid_position(grid, current_shape, shape_pos):
                        shape_pos[1] += 1
                if event.key == pygame.K_RIGHT:
                    shape_pos[1] += 1
                    if not valid_position(grid, current_shape, shape_pos):
                        shape_pos[1] -= 1
                if event.key == pygame.K_DOWN:
                    shape_pos[0] += 1
                    if not valid_position(grid, current_shape, shape_pos):
                        shape_pos[0] -= 1
                if event.key == pygame.K_UP:
                    current_shape = list(zip(*reversed(current_shape)))
                    if not valid_position(grid, current_shape, shape_pos):
                        current_shape = list(zip(*reversed(current_shape[::-1])))

        grid_copy = [row[:] for row in grid]
        merge_shape(grid_copy, current_shape, shape_pos)
        draw_grid()
        for y, row in enumerate(grid_copy):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, colors[cell], (x * block_size, y * block_size, block_size, block_size))

        pygame.display.update()

game()
pygame.quit()
