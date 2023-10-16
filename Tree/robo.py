import matplotlib.pyplot as plt
import numpy as np

from queue import PriorityQueue

def heuristic(position, goal):
    # Simple Manhattan distance heuristic
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def visualize_path(grid, path):
    grid_array = np.zeros_like(grid, dtype=np.uint8)

    for cell in grid:
        if grid[cell] == 1:  # Corrected obstacle representation
            grid_array[cell] = 1
        if grid[cell] == 'start':
            grid_array[cell] = 2
        if grid[cell] == 'goal':
            grid_array[cell] = 3

    for cell in path:
        grid_array[cell] = 4

    plt.imshow(grid_array, cmap='viridis')
    plt.colorbar()
    plt.title('Robot Path')
    plt.show()

def find_path(grid, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {cell: float('inf') for cell in grid}
    g_score[start] = 0

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            visualize_path(grid, path)  # Visualize the path
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current
            neighbor = (x + dx, y + dy)

            if neighbor in grid and grid[neighbor] != 1:  # Corrected obstacle representation
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    open_set.put((f_score, neighbor))

    return None  # No path found

# Example usage:
# Updated grid with a clear path
grid = {
    (0, 0): 'start',
    (3, 2): 'goal',
    (1, 1): 1,  # Corrected obstacle representation
    # ... other grid cells ...
}

start = (0, 0)
goal = (3, 2)

path = find_path(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
