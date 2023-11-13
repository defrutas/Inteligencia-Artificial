import pygame
from collections import deque

# Initialize Pygame
pygame.init()

# Constants for cell colors
WHITE = (255, 255, 255)  # Open cell
BLACK = (0, 0, 0)        # Obstacle
YELLOW = (255, 255, 0)    # Robot
GREEN = (0, 255, 0)       # Objective
RED = (255, 0, 0)         # Explored cell

def find_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    start = None
    end = None

    # Find the start and end positions
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 2:
                start = (i, j)
            elif matrix[i][j] == 3:
                end = (i, j)

    if start is None or end is None:
        return None

    queue = deque([(start[0], start[1], [])])

    while queue:
        row, col, path = queue.popleft()

        if (row, col) == end:
            return path + [(row, col)]

        if not visited[row][col]:
            visited[row][col] = True

            movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in movements:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and not visited[new_row][new_col]
                    and matrix[new_row][new_col] != 1
                ):
                    new_path = path + [(row, col)]
                    queue.append((new_row, new_col, new_path))
                    matrix[new_row][new_col] = 4  # Mark as explored

                    # Display the matrix with a delay
                    pygame.time.delay(0)  # Adjust the delay time in milliseconds

                    # Draw the matrix and update the display
                    screen.fill(WHITE)
                    for i in range(rows):
                        for j in range(cols):
                            color = WHITE if matrix[i][j] == 0 else BLACK if matrix[i][j] == 1 else YELLOW if matrix[i][j] == 2 else GREEN if matrix[i][j] == 3 else RED if matrix[i][j] == 4 else WHITE
                            pygame.draw.rect(screen, color, (j * (cell_size + margin), i * (cell_size + margin), cell_size, cell_size))

                    pygame.display.flip()

    return None

# Load the matrix from a file
file_path = 'matrix_files/matrix_44.txt'
with open(file_path, 'r') as file:
    matrix = [list(map(int, line.strip().split())) for line in file]

# Get the number of rows and columns
rows, cols = len(matrix), len(matrix[0])

# Set up display
cell_size = 10
margin = 1
width, height = cols * (cell_size + margin), rows * (cell_size + margin)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pathfinding Visualization')

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw the matrix
    for i in range(rows):
        for j in range(cols):
            color = WHITE if matrix[i][j] == 0 else BLACK if matrix[i][j] == 1 else YELLOW if matrix[i][j] == 2 else GREEN if matrix[i][j] == 3 else RED if matrix[i][j] == 4 else WHITE
            pygame.draw.rect(screen, color, (j * (cell_size + margin), i * (cell_size + margin), cell_size, cell_size))

    # Find and draw the path
    path = find_path(matrix)
    if path:
        for row, col in path:
            pygame.draw.rect(screen, RED, (col * (cell_size + margin), row * (cell_size + margin), cell_size, cell_size))

        # Draw the objective
        pygame.draw.rect(screen, GREEN, (path[-1][1] * (cell_size + margin), path[-1][0] * (cell_size + margin), cell_size, cell_size))

    pygame.display.flip()
    clock.tick(5)  # Adjust the speed of visualization (frames per second)

pygame.quit()
