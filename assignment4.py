import logging
logging.basicConfig(filename='assignment4.log',level=logging.INFO)

#1. Write a Python Program to Find the Factorial of a Number?
def fact(n):
    return 1 if (n==0 or n==1) else n * fact(n-1)
logging.info(fact(n=int(input('enter:'))))

#2. Write a Python Program to Display the multiplication Table?
def mult():
    n=int(input('enter number:'))
    for i in range(1,11):
         print(n,'x',i,'=',n*i)
mult()

#3. Write a Python Program to Print the Fibonacci sequence?
def fib(n):
    if n<0:
        return 'incorrect'
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
       return fib(n-1)+fib(n-2)
logging.info(fib(int(input('enter num:'))))

#4. Write a Python Program to Check Armstrong Number?
def armstrong():
    n=int(input('enter:'))
    s=n
    b=len(str(s))
    sum1=0
    while n!=0:
       r=n%10
       sum1=sum1+(r**b)
       n=n//10
    if s==sum1:
        return 'yes'
    else:
        return 'no'
logging.info(armstrong())


#5. Write a Python Program to Find Armstrong Number in an Interval?
def interval():
    lower=100
    upper=2000
    for num in range(lower,upper+1):
        order=len(str(num))
        sum=0
        temp=num
        while temp>0:
            digit=temp%10
            sum+=digit ** order
            temp=temp//10
        if num==sum:
            print (num)
interval()


#6. Write a Python Program to Find the Sum of Natural Numbers?
def sum():
    n=int(input('enter:'))
    return (int(n*(n+1))/2)
logging.info(sum())