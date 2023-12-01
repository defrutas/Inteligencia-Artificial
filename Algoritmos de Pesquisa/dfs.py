from collections import deque
import time

def dfs(matrix):
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
        return None, 0, 0  # No path found, return time and steps as 0

    stack = [(start[0], start[1], [])]

    start_time = time.time()

    while stack:
        row, col, path = stack.pop()

        if (row, col) == end:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return path + [(row, col)], elapsed_time, len(path) - 1  # Subtract 1 to exclude the starting position

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
                    new_path = path + [(new_row, new_col)]  # Increment step count only when adding to path
                    stack.append((new_row, new_col, new_path))
                    matrix[new_row][new_col] = 4  # Mark as explored

    return None, 0, 0  # No path found, return time and steps as 0

# Loop through matrices
with open('dfs.txt', 'w') as output_file:
    for matrix_number in range(1, 6):  # Adjust the range based on the number of matrices
        file_path = f'matrix_files/matrix_{matrix_number}.txt'

        with open(file_path, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]

        # Main algorithm
        path, elapsed_time, steps = dfs(matrix)

        # Print metrics
        output_file.write(f"\nMetrics for Matrix {matrix_number}:\n")
        if path:
            output_file.write(f"Final Path: {path}\n")
            output_file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")
            output_file.write(f"Number of Steps: {steps}\n")
        else:
            output_file.write("No path found.\n")
