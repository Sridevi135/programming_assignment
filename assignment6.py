import logging
logging.basicConfig(filename='assignment6.log',level=logging.INFO)




#1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def fib(n):
    if n<=1:
        return n
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
if True:
    n=int(input('enter:'))
    for i in range(n+1):
        logging.info(fib(i))



#2. Write a Python Program to Find Factorial of Number Using Recursion?
def fact(n):
    if n==1:
        return n
    elif n<0:
        return ('only positive')
    elif n==0:
        return ('the factorial of 0 is 1')
    else:
        return  n*fact(n-1)
n=int(input('enter:'))
logging.info(fact(n))




#3. Write a Python Program to calculate your Body Mass Index?
def bmi():
    height = float(input("Input your height in Feet: "))
    weight = float(input("Input your weight in Kilogram: "))
    bmi=round(weight / (height * height), 2)
    return  bmi
logging.info( bmi())





#4. Write a Python Program to calculate the natural logarithm of any number?
import math
def log():
    number=int(input('enter log number:'))
    n=math.log(number)
    return n
logging.info(log())





#5. Write a Python Program for cube sum of first n natural numbers?
def cube():
    n=int(input('enter:'))
    sum=0
    for i in range(1,n+1):
       sum=sum+(i*i*i)
    return sum
logging.info(cube())



