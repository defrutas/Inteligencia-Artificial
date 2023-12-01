import time

class DFSinMatrix:
    def hasPathDfs(self, adj):
        start_time = time.time()
        
        m = len(adj)
        n = len(adj[0])
        sx, sy, dx, dy = self.findSourceAndDest(adj, m, n)
        visited = [[False for i in range(n)] for j in range(m)]
        path = []  # Track the final path
        self.dfs(adj, sx, sy, dx, dy, visited, path)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if not path:
            return False, [], 0, elapsed_time
        return True, path, len(path), elapsed_time

    def dfs(self, adj, i, j, dx, dy, visited, path):
        m = len(adj)
        n = len(adj[0])
        if i < 0 or j < 0 or i > m - 1 or j > n - 1 or adj[i][j] == 1 or visited[i][j]:
            return False
        visited[i][j] = True
        if i == dx and j == dy:  # Reached destination
            path.append((i, j))
            return True
        
        if (self.dfs(adj, i - 1, j, dx, dy, visited, path) or
            self.dfs(adj, i + 1, j, dx, dy, visited, path) or
            self.dfs(adj, i, j - 1, dx, dy, visited, path) or
            self.dfs(adj, i, j + 1, dx, dy, visited, path)):
            path.append((i, j))  # Add the current position to the path
            return True
        
        return False

    def findSourceAndDest(self, adj, m, n):
        for i in range(m):
            for j in range(n):
                if adj[i][j] == 2:
                    sx, sy = i, j
                elif adj[i][j] == 3:
                    dx, dy = i, j
        return sx, sy, dx, dy


with open('dfs.txt', 'w') as output_file:
    for matrix_num in range(1, 50):  # Change the range as needed
        file_path = f'matrix_files/matrix_{matrix_num}.txt'
        
        with open(file_path, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]

        # find path
        g = DFSinMatrix()
        found, path, path_length, elapsed_time = g.hasPathDfs(matrix)

        if found:
            output_file.write(f"\nPath found in matrix {matrix_num} from robot to destination: \n")
            output_file.write(','.join([f"({i},{j})" for i, j in reversed(path)]))
            output_file.write(f"\nNumber of cells in the path: {path_length}\n")
            output_file.write(f"Elapsed time: {elapsed_time:.6f} seconds\n")
        else:
            output_file.write(f"\nNo path found in matrix {matrix_num} from robot to destination.\n")
