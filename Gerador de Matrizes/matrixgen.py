# Generate multiple randomized matrixes with 0s (empty spaces) 1s(obstacles)
# 2(robot placement) and 3(goal)
# to explore using AI algorithms
import random

# Define the dimensions of the matrix
rows, cols = 10, 10

# Define the number of matrices you want to generate
num_matrices = 10

# Open a text file for writing
with open('matrices.txt', 'w') as file:
    for matrix_num in range(1, num_matrices + 1):
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        # Generate random positions for the numbers 2 and 3
        position_2 = (random.randint(0, 9), random.randint(0, 9))
        position_3 = (random.randint(0, 9), random.randint(0, 9))

        # Fill the matrix with 1s, 2, and 3
        for i in range(rows):
            for j in range(cols):
                if (i, j) == position_2:
                    matrix[i][j] = 2
                elif (i, j) == position_3:
                    matrix[i][j] = 3
                else:
                    matrix[i][j] = random.randint(0, 1)

        # Write the matrix to the file
        file.write(f"Matrix {matrix_num}:\n")
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
        file.write('\n')

print("Matrices saved to matrices.txt")
