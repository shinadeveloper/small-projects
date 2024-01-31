import numpy as np

def initialize(dim):
  l=[]
  for i in range(dim):
    l.append([])
    for j in range(dim):
      l[i].append(0)
  return l
def matrix_multiplication(m,n):
  dim=len(m)
  l=initialize(dim)
  for i in range(dim):
    for j in range(dim):
      for k in range(dim):
        l[i][j]=l[i][j]+m[i][k]*n[k][j]
  return l

a=[[1,2],[3,4]]
b=[[3,4],[4,5]]
print(matrix_multiplication(a,b))

def row(matrix,i):
  dim=len(matrix)
  l=[]
  for k in range(dim):
    l.append(matrix[i][k])
  return l

def column(matrix,j):
  dim=len(matrix)
  l=[]
  for k in range(dim):
    l.append(matrix[k][j])
  return l

def dotproduct(row,column):
  dim=len(row)
  sum=0
  for i in range(dim):
   sum=sum+(row[i]*column[i])
  return sum
  
def matrix_multiplication_using_functions(matrix1,matrix2):
  dim=len(matrix1)
  l=initialize(dim)
  for i in range(dim):
    for j in range(dim):
      l[i][j]=l[i][j]+dotproduct(row(matrix1,i),column(matrix2,j))
  return l

c=np.matrix(a)
d=np.matrix(b)
e=c*d
print(e)


print(matrix_multiplication_using_functions(a,b))
#n=int(input())
#m=initialize(n)
#print(m)
      
