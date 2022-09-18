import logging
logging.basicConfig(filename='assignment2.log',level=logging.INFO)

#1. Write a Python program to convert kilometers to miles?
import logging
def kmtomiles():
    km=int(input('kilometer:'))
    cn=0.621371
    miles=km*cn
    return miles
logging.info(kmtomiles())



#2. Write a Python program to convert Celsius to Fahrenheit?
def celtofah():
    celsius=int(input('celsius:'))
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
logging.info(celtofah())



#3. Write a Python program to display calendar?
import calendar
year=int(input('enter year'))
month=int(input('enter month'))
logging.info(calendar.month(year,month))



#4. Write a Python program to solve quadratic equation?
import cmath
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
def fun():
    dis = (b**2) - (4 * a*c)
    ans1 = (-b-cmath.sqrt(dis))/(2 * a)
    ans2 = (-b + cmath.sqrt(dis))/(2 * a)
    return('the roots are',ans1,ans2)
logging.info(fun())



#5. Write a Python program to swap two variables without temp variable?
def swap():
    a=int(input('num1:'))
    b=int(input('num2:'))
    a,b=b,a
    return a,b
logging.info(swap())






