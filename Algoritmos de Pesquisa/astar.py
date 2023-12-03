import heapq
import time

def find_start_end(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start, end = None, None

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 2:
                start = (i, j)
            elif matrix[i][j] == 3:
                end = (i, j)

    return start, end

def astar(matrix):
    start_time = time.time()

    start, end = find_start_end(matrix)
    
    if not start or not end:
        return None, None, None  # Start or end not found in the matrix

    rows, cols = len(matrix), len(matrix[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == end:
            path = reconstruct_path(came_from, end)
            end_time = time.time()
            return path, end_time - start_time, len(path) - 1  # Return path, time taken, and number of steps

        for neighbor in get_neighbors(current_node, rows, cols):
            tentative_g_score = g_score[current_node] + 2 if is_turn(current_node, neighbor) else g_score[current_node] + 1

            if matrix[neighbor[0]][neighbor[1]] == 1:  # Skip obstacles
                continue

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current_node

    return None, None, None  # No path found

def is_turn(current, neighbor):
    return current[0] != neighbor[0] and current[1] != neighbor[1]

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from and came_from[current] is not None:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, rows, cols):
    i, j = node
    neighbors = []

    if i > 0:
        neighbors.append((i - 1, j))
    if i < rows - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < cols - 1:
        neighbors.append((i, j + 1))

    return neighbors

# Example usage:
with open('astar.txt', 'w') as output_file:
    total_time_taken = 0
    total_num_steps = 0

    for matrix_number in range(1, 50):  # Adjust the range based on the number of matrices
        file_path = f'matrix_files/matrix_{matrix_number}.txt'
        with open(file_path, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]

        path, time_taken, num_steps = astar(matrix)

        if path:
            total_time_taken += time_taken
            total_num_steps += num_steps
            output_file.write(f"Matrix {matrix_number}:\n")
            output_file.write(f"Time taken: {time_taken} seconds\n")
            output_file.write(f"Number of steps in the shortest path: {num_steps}\n")
            output_file.write("\n")
        else:
            output_file.write(f"No path found for Matrix {matrix_number}\n\n")

    # Calculate averages
    if total_time_taken > 0:
        average_time_taken = total_time_taken / 49  # Adjust the denominator based on the actual number of matrices
        average_num_steps = total_num_steps / 49  # Adjust the denominator based on the actual number of matrices

        # Print average metrics
        output_file.write("\nAverage Metrics for All Matrices:")
        output_file.write(f"\nAverage Time Taken: {average_time_taken} seconds")
        output_file.write(f"\nAverage Number of Steps in the Shortest Path: {average_num_steps}\n")
    else:
        output_file.write("\nNo matrices found.\n")
