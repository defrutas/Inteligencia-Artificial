# def color_map(graph):
#     colors = {}  # Dictionary to store the colors of each region

#     for region in graph:
#         available_colors = set(range(1, 5))  # 4 colors available
#         for neighbor in graph[region]:
#             if neighbor in colors:
#                 available_colors.discard(colors[neighbor])

#         if available_colors:
#             colors[region] = min(available_colors)
#         else:
#             # No available colors, backtrack or adjust colors as needed
#             pass  # You can add backtracking logic here

#     return colors

# # Example map as a graph
# map_graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D'],
#     'D': ['B', 'C']
# }

# coloring = color_map(map_graph)
# print(coloring)

def is_safe(graph, v, color, c):
    for neighbor in graph[v]:
        if neighbor == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, num_colors):
    V = len(graph)
    color = [-1] * V  # Initialize colors for all vertices

    def solve(v):
        if v == V:
            return True

        for c in range(num_colors):
            if is_safe(graph, v, color, c):
                color[v] = c
                if solve(v + 1):
                    return True
                color[v] = -1  # Backtrack

    if not solve(0):
        print("No solution exists")
        return
    else:
        print("Solution exists:")
        for c in color:
            print(c, end=" ")

# Example usage:
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
num_colors = 4

graph_coloring(graph, num_colors)

