import heapq

# Define the matrix
matrix = [
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 3],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 2, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0]
]

# Define possible movements
movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Function to calculate the heuristic (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Function to find the optimal path
def find_optimal_path(matrix):
    start = None
    goal = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                start = (i, j)
            elif matrix[i][j] == 3:
                goal = (i, j)
    
    if start is None or goal is None:
        return None
    
    open_list = [(0, start)]
    closed_list = set()
    came_from = {}
    g_score = {position: float('inf') for row in matrix for position in row}
    g_score[start] = 0
    f_score = {position: float('inf') for row in matrix for position in row}
    f_score[start] = heuristic(start, goal)
    
    while open_list:
        current_f, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        closed_list.add(current)
        
        for dx, dy in movements:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if neighbor[0] < 0 or neighbor[0] >= len(matrix) or neighbor[1] < 0 or neighbor[1] >= len(matrix[0]):
                continue
            
            if matrix[neighbor[0]][neighbor[1]] == 1 or neighbor in closed_list:
                continue
            
            tentative_g_score = g_score[current] + 1
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_list:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None

# Find and print the optimal path
optimal_path = find_optimal_path(matrix)
if optimal_path:
    print("Optimal Path:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) == optimal_path[0]:
                print("2", end=" ")
            elif (i, j) == optimal_path[-1]:
                print("3", end=" ")
            elif (i, j) in optimal_path:
                print("X", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()
else:
    print("No path found.")
