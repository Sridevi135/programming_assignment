#1. Write a Python program to find sum of elements in list?
l=[8,3,1,5,4]
def sum():
    x=0
    for i in l:
        x=x+i
        i+=1
    return x
print(sum())



#2. Write a Python program to Multiply all numbers in the list?
a=[9,3,5,1,9]
def mul():
    x=1
    for i in a:
        x=x*i
        i+=1
    return x
print(mul())


#3. Write a Python program to find smallest number in a list?
a=[9,43,87,2,56]
s=[]
def small():
    for i in a:
        s.append(i)
    return min(s)
print(small())

#4. Write a Python program to find largest number in a list?
a=[9,45,12,84,2]
def maxi():
    mx=a[0]
    for x in a:
        if x>mx:
            mx=x
    return mx
print(maxi())


#5. Write a Python program to find second largest number in a list?
list1 = [10, 20, 4, 45, 99]
mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
            mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and \
            secondmax != list1[i]:
        secondmax = list1[i]
print("Second highest number is : ", (secondmax))


#6. Write a Python program to find N largest elements from a list?
def Nmaxelements(list1, N):
    final_list = []
    for i in range(0, N):
        max1 = 0
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];
        list1.remove(max1);
        final_list.append(max1)
    print(final_list)
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 5
Nmaxelements(list1, N)



#7. Write a Python program to print even numbers in a list?
l=[3,7,5,6,1,8,34,63,23,99,100]
def even():
    e=[]
    for i in l:
        if i%2==0:
            e.append(i)
    return e
print(even())


#8. Write a Python program to print odd numbers in a List?
l=[3,7,5,6,1,8,34,63,23,99,100]
def odd():
    e=[]
    for i in l:
        if i%2!=0:
            e.append(i)
    return e
print(odd())

#9. Write a Python program to Remove empty List from List?
def empty_list_remove(input_list):
    new_list = []
    for ele in input_list:
        if ele:
            new_list.append(ele)
    return new_list
input_list = [5, 6, [], 3, [], [], 9]
print(empty_list_remove(input_list))



#10. Write a Python program to Cloning or Copying a list?
l=[9,3,5,1,4]
def cloning(l):
    new_list=l[:]
    return new_list
new_list=cloning(l)
print(new_list)


#11. Write a Python program to Count occurrences of an element in a list?
l=[9,4,6,9,1,4,6,6,8]
x=6
def countx():
    count=0
    for i in l:
        if i==x:
            count+=1
    return x,count
print(countx())