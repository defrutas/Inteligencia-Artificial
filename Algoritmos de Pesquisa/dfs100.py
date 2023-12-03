import time

class DFSinMatrix:
    def hasPathDfs(self, adj):
        start_time = time.time()

        m = len(adj)
        n = len(adj[0])
        sx, sy, dx, dy = self.findSourceAndDest(adj, m, n)
        visited = [[False for i in range(n)] for j in range(m)]
        stack = [(sx, sy)]
        path = []  # Track the final path

        while stack:
            i, j = stack.pop()
            if not (0 <= i < m) or not (0 <= j < n) or adj[i][j] == 1 or visited[i][j]:
                continue

            visited[i][j] = True
            path.append((i, j))

            if i == dx and j == dy:  # Reached destination
                end_time = time.time()
                elapsed_time = end_time - start_time
                return True, path[::-1], len(path), elapsed_time

            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))

        end_time = time.time()
        elapsed_time = end_time - start_time

        return False, [], 0, elapsed_time

    def findSourceAndDest(self, adj, m, n):
        for i in range(m):
            for j in range(n):
                if adj[i][j] == 2:
                    sx, sy = i, j
                elif adj[i][j] == 3:
                    dx, dy = i, j
        return sx, sy, dx, dy

with open('dfs100.txt', 'w') as output_file:
    for matrix_num in range(1, 50):  # Change the range as needed
        file_path = f'matrix_files100x100/matrix_{matrix_num}.txt'

        with open(file_path, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]

        # find path
        g = DFSinMatrix()
        found, path, path_length, elapsed_time = g.hasPathDfs(matrix)

        if found:
            output_file.write(f"\nPath found in matrix {matrix_num} from robot to destination:")
            output_file.write(f"\nNumber of cells in the path: {path_length}\n")
            output_file.write(f"Elapsed time: {elapsed_time:.6f} seconds\n")
        else:
            output_file.write(f"\nNo path found in matrix {matrix_num} from robot to destination.\n")
