import logging
logging.basicConfig(filename="assignment1.log",level=logging.INFO)


#1. Write a Python program to print "Hello Python"?
def justprint():
    return "Hello Python"
logging.info(justprint())


#2. Write a Python program to do arithmetical operations addition and division.?
def arithmetic():
    a=3
    b=5
    return a+b,a-b,a/b,a*b
logging.info(arithmetic())


#3. Write a Python program to find the area of a triangle?
def area():
    breath=int(input('enter breath:'))
    height=int(input('enter height:'))
    num=(breath*height)/2
    return num
logging.info(area())


#4. Write a Python program to swap two variables?
def swap():
    a=int(input('num1:'))
    b=int(input('num2:'))
    temp=a
    a=b
    b=temp
    return a,b
logging.info(swap())


#5. Write a Python program to generate a random number?
import random
num=random.random()
logging.info(num)