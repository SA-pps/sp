# Program to find the REF or RREF form of a given matrix
m = int(input("Enter the number of rows : "))
n = int(input("Enter the number of columns : "))

matrix = list()
temp = list()
equation_type = 0

zero_div_error = False

# getting the matrix as input
for i in range(m):
    temp.clear()
    for j in range(n):
        temp.append(float(input(f"Enter the element in row {i+1} | column {j+1} : ")))
    matrix.append(temp.copy())
    print("\n")

lead = 0
loop = True

# finding the RREF form of the given matrix
for r in range(m):
    if lead >= n:
        break

    i = r
    while matrix[i][lead] == 0.0:
        i += 1
        if i == m:
            i = r
            lead += 1
            if n == lead:
                loop = False
                break

    if not loop:
        break

    matrix[i], matrix[r] = matrix[r], matrix[i]
    first_val = matrix[r][lead]
    matrix[r] = [x/float(first_val) for x in matrix[r]]

    for i in range(m):
        if i != r:
            first_val = matrix[i][lead]
            matrix[i] = [y - first_val*x for x, y in zip(matrix[r], matrix[i])]
    lead += 1

rank = 0
# displaying the matrix
print("RREF form : ")
for row in matrix:
    if (sum(row) != 0.0):
        rank += 1
    print("\t".join(f"{x+0.0:.2f}" for x in row))
print(f"\nRank = {rank}")
