n = int(input("Enter the number of equations or variables : "))
error = float(input("Enter the error of tolerance : "))

augmented_matrix = list()
temp = list()

# getting the equations in the form of an augmented matrix
for i in range(n):
    temp.clear()
    for j in range(n):
        temp.append(float(input(f"Enter the coefficient {j+1} of equation {i+1} : ")))
    temp.append(float(input(f"Enter the result of equation {i+1} : ")))
    augmented_matrix.append(temp.copy())

# converting the augmented matrix to diagonally dominant form
for i in range(n):
    index = augmented_matrix[i].index(max(augmented_matrix[i][:n]))
    if index != i:
        augmented_matrix[i], augmented_matrix[index] = augmented_matrix[index], augmented_matrix[i]

X = [0] * n
prev_X = [0] * n
condition = True
isInvalid = False
count = 0

print('count\t{}'.format("\t".join(f"var{i}" for i in range(1,n+1))))
# performing Gauss-Seidel method to find the unknowns
while (condition):
    for i in range(n):
        sum = 0.0
        c = 0
        
        #condition where Gauss-Seidel method fails
        if augmented_matrix[i][i] == 0.0:
            print("Gauss-Seidel method fails for the given system.")
            isInvalid = True
            break
        
        if isInvalid:
            break
        
        for j in range(n):
            if i != j:
                sum += augmented_matrix[i][j] * X[j]
        X[i] = (augmented_matrix[i][n] - sum) / augmented_matrix[i][i]
    count += 1
    print('{}\t{}'.format(count, "\t".join(f"{x:.4f}" for x in X)))
    for k in range(n):
        if abs(prev_X[k]-X[i]) <= error:
            condition = False
    prev_X = X.copy()
        

# Displaying the matrix
print("\nResult : ")
for i in range(n):
    print(f"variable {i+1} = {X[i]}")
