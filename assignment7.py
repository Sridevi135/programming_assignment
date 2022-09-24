import logging
logging.basicConfig(filename='assignment7.log',level=logging.INFO)


#1. Write a Python Program to find sum of array?
size=int(input('enter array size:'))
def arr():
    sum=0
    for i in range(size):
        num=int(input('enter elements:'))
        sum=sum+num
    return sum
logging.info(arr())



#2. Write a Python Program to find largest element in an array?
size=int(input('no of elements:'))
l=[]
def lar():
    for i in range(size):
        elements=int(input('elements of array'))
        l.append(elements)
    return max(l)
logging.info(lar())



#3. Write a Python Program for array rotation?
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr = arr[: i] + temp
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
logging.info(rotateArray(arr, len(arr), 3))



#4. Write a Python Program to Split the array and add the first part to the end?
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = x
    return arr
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
logging.info(splitArr(arr,n,position))


#5. Write a Python Program to check if given array is Monotonic?
def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
A = [6, 5, 4, 9]
logging.info(isMonotonic(A))
