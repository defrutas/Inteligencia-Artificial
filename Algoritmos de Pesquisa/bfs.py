from collections import deque
import time

def bfs(matrix):
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

    queue = deque([(start[0], start[1], [])])

    start_time = time.time()

    while queue:
        row, col, path = queue.popleft()

        if (row, col) == end:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return path + [(row, col)], elapsed_time, len(path)

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

    return None, 0, 0  # No path found, return time and steps as 0

# Open the bfs.txt file in append mode
with open('bfs.txt', 'w') as bfs_file:
    total_elapsed_time = 0
    total_steps = 0

    # Loop through matrices
    for matrix_number in range(1, 50):  # Adjust the range based on the number of matrices
        file_path = f'matrix_files/matrix_{matrix_number}.txt'

        with open(file_path, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]

        # Get the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # Main algorithm
        path, elapsed_time, steps = bfs(matrix)

        # Print metrics
        print(f"\nMetrics for Matrix {matrix_number}:", file=bfs_file)
        if path:
            print(f"Elapsed Time: {elapsed_time:.10f} seconds", file=bfs_file)
            print("Number of Steps:", steps, file=bfs_file)
            total_elapsed_time += elapsed_time
            total_steps += steps
        else:
            print("No path found.", file=bfs_file)

    # Calculate averages
    if total_elapsed_time > 0:
        average_elapsed_time = total_elapsed_time / 49  # Adjust the denominator based on the actual number of matrices
        average_steps = total_steps / 49  # Adjust the denominator based on the actual number of matrices

        # Print average metrics
        print("\nAverage Metrics for All Matrices:", file=bfs_file)
        print(f"Average Elapsed Time: {average_elapsed_time:.10f} seconds", file=bfs_file)
        print("Average Number of Steps:", average_steps, file=bfs_file)
    else:
        print("\nNo matrices found.", file=bfs_file)