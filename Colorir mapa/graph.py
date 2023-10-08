# Vertices - number of countries
vertices = {
    'P': 0,     #Portugal
    'S': 1,     #Spain
    'F': 2,     #France
    'B': 3,     #Belgium
    'N': 4,     #Netherlands
    'G': 5,     #Germany
    'SW': 6,    #Switzerland
    'I': 7,     #Italy
}

# Edges - adjacent countries
edges = [
    ('P', 'S'),
    ('S', 'F'),
    ('F', 'B'),
    ('F', 'G'),
    ('F', 'S'),
    ('F', 'I'),
    ('B', 'N'),
    ('B', 'F'),
    ('B', 'G'),
    ('N', 'B'),
    ('N', 'G'),
    ('G', 'N'),
    ('G', 'B'),
    ('G', 'F'),
    ('G', 'S'),
    ('SW', 'G'),
    ('SW', 'F'),
    ('SW', 'I'),
    ('I', 'F'),
    ('I', 'S'),
]

# Create an adjacency matrix to represent the graph
V = len(vertices)
graph = [[0 for _ in range(V)] for _ in range(V)]

# Fill in the adjacency matrix based on the edges
for edge in edges:
    v1, v2 = vertices[edge[0]], vertices[edge[1]]
    graph[v1][v2] = 1
    graph[v2][v1] = 1  # Assuming the graph is undirected
# The 'graph' variable now represents the adjacency matrix of your map.

#Display matrix
for row in graph:
    print(row)