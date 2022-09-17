#1. Write a Python program to print "Hello Python"?
import logging
logging.basicConfig(filename="assignment1.log",level=logging.INFO)
logging.info('This is my first code')
def justprint():
    return "Hello Python"
#print(justprint())
logging.info(justprint())


#2. Write a Python program to do arithmetical operations addition and division.?
def arithmetic():
    a=3
    b=5
    return a+b,a-b,a/b,a*b
#print(arithmetic())
logging.info(arithmetic())


#3. Write a Python program to find the area of a triangle?
def swap():
    a=10
    b=20
    a,b=b,a
    return a,b
#print(swap())
logging.info(swap())


#4. Write a Python program to swap two variables?
import random
num=random.random()
logging.info(num)


#5. Write a Python program to generate a random number?
def area():
    breath=int(input('enter breath'))
    height=int(input('enter height:'))
    area=(breath*height)/2
    return area
#print(area())
logging.info(area())
