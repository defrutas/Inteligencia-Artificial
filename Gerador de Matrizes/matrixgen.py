import random
import os

# Define the dimensions of the matrix
rows, cols = 50, 50

# Define the number of matrices you want to generate
num_matrices = 50

# Define the probability of generating a 1 (obstacle)
obstacle_probability = 0.3  # Adjust this value as needed (e.g., 0.2 for 20% obstacles)

# Create a directory to store the matrix files
if not os.path.exists("matrix_files"):
    os.mkdir("matrix_files")

for matrix_num in range(1, num_matrices + 1):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Generate random positions for the numbers 2 and 3
    position_2 = (random.randint(0, 49), random.randint(0, 49))
    position_3 = (random.randint(0, 49), random.randint(0, 49))

    # Fill the matrix with 1s, 2, and 3 with adjusted obstacle probability
    for i in range(rows):
        for j in range(cols):
            if (i, j) == position_2:
                matrix[i][j] = 2
            elif (i, j) == position_3:
                matrix[i][j] = 3
            else:
                if random.random() < obstacle_probability:
                    matrix[i][j] = 1

    # Create a folder for the current matrix
    # folder_name = os.path.join("matrix_files", f"matrix_{matrix_num}")
    # os.mkdir(folder_name)

    # Write the matrix to a text file in the folder
    file_path = os.path.join("matrix_files", f"matrix_{matrix_num}.txt")
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

print("Matrices saved in separate folders.")
