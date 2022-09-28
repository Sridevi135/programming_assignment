'''Question 1:

Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''

import math
c=50
h=30
d=input("enter any values").split(',')
for i in d:
  sq=math.sqrt((2*c*float(i))/h)
  print (sq)

'''Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''

user_input = input("Enter values for row and column number: ")
rows, cols = user_input.split(",")
rows = int(rows)
cols = int(cols)

grid = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(x * y)
    grid.append(row)
    print(row)
print()
print(grid)

'''Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

phrase = input("Input words: ")

phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))

'''Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''

phrase = input("Type in: ")
phrase_splited = phrase.split(' ')
word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))

'''Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

'''Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''

s=input("enter sequence of comma separated passwords :")
import re
l=s.split(",")
for i in l:
    if(len(i)>=6 and len(i)<=12):
        if re.search("([a-z])+",i):
            if re.search("([A-Z])+", i):
                if re.search("([0-9])+", i):
                    if re.search("([#,@,$])+", i):
                        print(i)