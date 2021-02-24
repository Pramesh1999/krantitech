# initializing an empty matrix
matrix1 = []
# taking 3x3 matrix from the user
for i in range(3):
   # empty row
   row = []
   for j in range(3):
      # asking the user to input the number
      # converts the input to int as the default one is string
      element = int(input())
      # appending the element to the 'row'
      row.append(element)
   # appending the 'row' to the 'matrix'
   matrix1.append(row)
# printing the matrix
print(matrix1)

# initializing an empty matrix
matrix2 = []
# taking 3x3 matrix from the user
for i in range(3):
   # empty row
   row = []
   for j in range(3):
      # asking the user to input the number
      # converts the input to int as the default one is string
      element = int(input())
      # appending the element to the 'row'
      row.append(element)
   # appending the 'row' to the 'matrix'
   matrix2.append(row)
# printing the matrix
print(matrix2)

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# iterate through rows
for i in range(len(matrix1)):
    # iterate through columns
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
for r in result:
    print(r)
    
    
    #OUT PUT
"""
1
2
3
4
5
6
7
8
9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
9
8
7
6
5
4
3
2
1
[[9, 8, 7], [6, 5, 4], [3, 2, 1]]
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]

"""
    
    
