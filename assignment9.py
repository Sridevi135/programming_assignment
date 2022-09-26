#1. Write a Python program to check if the given number is a Disarium Number?
import math
def check(n):
    count_digits=len(str(n))
    sum=0
    x=n
    while(x!=0):
        r=x%10
        sum=(sum+math.pow(r,count_digits))
        count_digits=count_digits-1
        x=x//10
    if sum==n:
        return 1
    else:
        return 0
n=135
if (check(n)==1):
    print('disarium number')
else:
    print('not a disarium number')




#2. Write a Python program to print all disarium numbers between 1 to 100?
import math
def check(n):
    count_digits=len(str(n))
    sum=0
    x=n
    while(x!=0):
        r=x%10
        sum=(sum+math.pow(r,count_digits))
        count_digits=count_digits-1
        x=x//10
    return sum
result=0
for i in range(1,101):
    result=check(i)
    if result==i:
        print(i)


#3. Write a Python program to check if the given number is Happy Number?
def is_happy(n):
    past=set()
    while n!=1:
        n=sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
print(is_happy(6))
print(is_happy(7))


#4. Write a Python program to print all happy numbers between 1 and 100?
def check_happy(number):
  remainder = 0
  happy_num = 0;
  while(number > 0):
    remainder = number%10;
    happy_num = happy_num + (remainder*remainder);
    number = number//10;
  return happy_num;
lower = int(input("ENTER LOWEST VALUE : "))
upper = int(input("ENTER HIGHEST VALUE : "))
print("HAPPY NUMBERS WITHIN RANGE({},{}) ARE -".format(lower,upper))
for i in range(lower,upper+1):
  happy_num = i
  while(happy_num != 1 and happy_num != 4):
    happy_num = check_happy(happy_num)
  if(happy_num == 1):
    print(i,end=" ")



#5. Write a Python program to determine whether the given number is a Harshad Number?
def check(n):
    sum=0
    temp=n
    while temp>0:
        sum=sum+temp%10
        temp=temp//10
    return n%sum==0
if(check(12)):
    print('yes')
else:
    print('no')
#if(check(15)):
    #print('yes')
#else:
    #print('no')





#6. Write a Python program to print all pronic numbers between 1 and 100?
def pronic(num):
    flag=False
    for j in range(1,num+1):
        if j*(j+1)==num:
            flag=True
            break
    return flag
for i in range(1,100):
    if(pronic(i)):
        print(i,end=' ')