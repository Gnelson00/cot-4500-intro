import numpy as np

#Question 1
#this is just creating the standard 3x3 matrix
matrixOne = np.identity(3)
print(matrixOne)
print()

#Question 2
#Now we are adding 3 to all values not along the diagonal
matrixTwo = matrixOne
matrixTwo[matrixTwo != 1] += 3
print(matrixTwo)
print()

#Question 3
#This is getting rid of the 3rd column from the matrix above
matrixThree = np.delete(matrixTwo, -1, 1)
print(matrixThree)
