#1. Write a Python Program to Add Two Matrices?
def mat():
    x=[[1,2,3],
       [4,5,6],
       [7,8,9]]
    y=[[9,8,7],
       [6,5,4],
       [3,2,1]]
    result=[[0,0,0],
            [0,0,0],
            [0,0,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j]=x[i][j]+y[i][j]
    for r in result:
        return result
print(mat())



#2. Write a Python Program to Multiply Two Matrices?
a=[[8,12,7,3,2],
   [8,4,5,6,2],
   [8,7,8,9,2]]
b=[[5,8,1,2],
   [6,7,3,0],
   [4,5,9,1]]
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range (len(a)):
    for j in range (len(b[0])):
        for k in range(len(b)):
            result[i][j]+=a[i][k]*b[k][j]
print('the matrix is')
for r in result:
    print(r)


#3. Write a Python Program to Transpose a Matrix?
n=4
def transpose(a):
    for i in range(n):
        for j in range(i+1,n):
            a[i][j],a[j][i]=a[j][i],a[i][j]
a = [ [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
transpose(a)
print('modified matrix is')
for i in range(n):
    for j in range(n):
        print(a[i][j]," ",end='')
    print()



#4. Write a Python Program to Sort Words in Alphabetic Order?
def func(s):
    w=s.split(' ')
    for i in range(len(w)):
        w[i]=w[i].lower()
    s=sorted(w)
    print(' '.join(s))
s='the quick brown fox jumps over the laze dog'
func(s)




#5. Write a Python Program to Remove Punctuation From a String?
import re
test='hii!! this, is ,sri. devi;'
res=re.sub(r'[^\w\s]','',test)
print(res)