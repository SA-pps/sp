n1=int(input("Enter how many equations :"))
n2=int(input("Enter how many variables :"))
matrix=[]
for i in range(0,n1):
    r=[]
    for j in range(0,n2):
        print("Enter coeiff of variable",j+1,end=" ")
        r.append(int(input()))
    print("Enter coeiff of constant ",i+1,end=" ")
    r.append(int(input()))
    matrix.append(r)

print("AUGMENTED MATRIX:")
for i in range(n1):
    for j in range(n2+1):
        print(matrix[i][j], end = " ")
    print()
