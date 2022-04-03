# Program to find the solution for a system of linear equations with a unique solution
n = int(input("Enter the number of equations or variables : "))

augmented_matrix = list()
temp = list()
equation_type = 0

zero_div_error = False

# getting the augmented matrix as input
for i in range(n):
    temp.clear()
    for j in range(n):
        temp.append(
            float(input(f"Enter the coefficient of variable {j+1} in equation{i+1} : ")))
    temp.append(float(input(f"Enter the output of equation {i+1} : ")))
    augmented_matrix.append(temp.copy())
    print("\n")

# converting the augmented matrix to REF or RREF form
for i in range(n):

    # taking all the row(s) leading with zero(s) to last row(s)
    if augmented_matrix[i][i] == 0.0:
        c = 1
        while ((i+c) < n and augmented_matrix[i+c][i] == 0):
            c += 1

        # this condition implies the case where we have row(s) with all zero entries
        if (i+c == n):
            equation_type = 1
            break

        augmented_matrix[i], augmented_matrix[i + c] = augmented_matrix[i+c], augmented_matrix[i]

    # reducing the row
    for j in range(n):
        if i != j:
            ratio = augmented_matrix[j][i] / augmented_matrix[i][i]

            for k in range(n+1):
                augmented_matrix[j][k] = augmented_matrix[j][k] - ratio * augmented_matrix[i][k]

temp_sum = 0
j = 0

# finding the equation type
if (equation_type == 1):
    equation_type = 3
    for i in range(n):
        sum = 0
        while(j < n):
            sum += augmented_matrix[i][j]
            j += 1
        if (sum == augmented_matrix[i][j+1]):
            equation_type = 2

# checking the type of the equation
if equation_type == 2:
    print("The equation has infinitly many solutions.")
elif equation_type == 3:
    print("The equation has no solution.")
else:
    for i in range(n):
        print(
            f"variable {i+1} = {augmented_matrix[i][n]/augmented_matrix[i][i]}")
