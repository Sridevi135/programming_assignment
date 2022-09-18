import logging
logging.basicConfig(filename='assignment3.log',level=logging.INFO)

#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
def check():
    num=int(input(('enter num:')))
    if num>0: return 'positive'
    elif num<0: return 'negative'
    else: return 'zero'
logging.info(check())


#2. Write a Python Program to Check if a Number is Odd or Even?
def evenorodd():
    number=int(input('enter number to check:'))
    if number%2==0: return 'even'
    else: return 'odd'
logging.info(evenorodd())



#3. Write a Python Program to Check Leap Year?
def leapyear():
    year=int(input('enter year:'))
    if year%2==0:
        if year%100==0 and year%400==0:
            return 'leap year'
        else:
            return 'not leap year'
    else:
       return 'not leap year'
logging.info(leapyear())


#4. Write a Python Program to Check Prime Number?
def prime():
    num=int(input('enter num:'))
    if num>0:
        for i in range (2,num):
            if num%i==0:
                return 'not a prime number'
            return 'it is a prime number'
logging.info(prime())



#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
def is_prime():
    l=1
    h=10000
    k=[]
    for num in range(l,h):
        if(num>1):
            for i in range(2,(num//2)+1):
                if(num%i)==0:
                    break
            else:
                k.append(num)
    return k

logging.info(is_prime())