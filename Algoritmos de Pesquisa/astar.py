import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def heuristic(start, goal):
    # Manhattan distance
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def astar(matrix):
    rows, cols = len(matrix), len(matrix[0])
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

    priority_queue = [(0, start, [], 0)]  # Add the cost parameter to the priority queue
    heapq.heapify(priority_queue)

    visited = set()

    while priority_queue:
        _, current, path, cost = heapq.heappop(priority_queue)

        matrix[current[0]][current[1]] = 'x'  # Mark as explored

        if current == end:
            print_path(matrix, path)
            return path + [current], cost  # Return the path and the total cost

        if current not in visited:
            visited.add(current)

            movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in movements:
                new_row, new_col = current[0] + dr, current[1] + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and matrix[new_row][new_col] != 1
                ):
                    new_path = path + [current]
                    new_cost = cost + 1  # Base cost for moving straight

                    # Update the Node class instantiation
                    neighbor = Node(parent=current, position=(new_row, new_col))
                    neighbor.g = new_cost
                    neighbor.h = heuristic((new_row, new_col), end)
                    neighbor.f = neighbor.g + neighbor.h

                    if neighbor.position not in visited:
                        visited.add(neighbor.position)
                        matrix[new_row][new_col] = 'x'  # Mark as explored
                        heapq.heappush(priority_queue, (neighbor.f, neighbor.position, new_path, new_cost))

            print_matrix(matrix)

    return None, 0  # Return None and 0 if no path is found

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

def print_path(matrix, path):
    for row, col in path:
        matrix[row][col] = '*'
    print_matrix(matrix)

# Load the matrix from a file
file_path = 'matrix_files/matrix_1.txt'
with open(file_path, 'r') as file:
    matrix = [list(map(int, line.strip().split())) for line in file]

# Get the number of rows and columns
rows, cols = len(matrix), len(matrix[0])

path, total_cost = astar(matrix)
