#1. Write a Python program to find words which are greater than given length k?
word='hello guys how are you people doing'
k=3
print([words for words in word.split() if len(words)>k])


#2. Write a Python program for removing i-th character from a string?
def remove():
    i = 5
    n = 'extrodinary'
    for j in range(len(n)):
        if j==i:
            n=n.replace(n[j],"",1)
    return n
print(remove())

#3. Write a Python program to split and join a string?
def split(string):
    list_string=string.split()
    return list_string
def join1(list_string):
    string='-'.join(list_string)
    return string
string='sri devi'
list_string=split(string)
string=join1(list_string)
print(string)
print(list_string)



#4. Write a Python to check if a given string is binary string or not?
n='sride01'
import re
c=re.compile('[^01]')
if len(c.findall(n)):
    print('no')
else:
    print('yes')
#5. Write a Python program to find uncommon words from two Strings?




#6. Write a Python to find all duplicate characters in string?
def uncommon(a,b):
    count={}
    for word in a.split():
        count[word]=count.get(word,0)+1
    for word in b.split():
        count[word]=count.get(word,0)+1
    return [word for word in count if count[word]==1]
a='geeks for geeks'
b='learn until you learn'
print(uncommon(a,b))


#7. Write a Python Program to check if a string contains any special character?
import re
def reg(string):
    regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(string)==None):
        return('string is accepted')
    else:
        return('string is not accepted')
string='geeks*&6for$%%geeks'
print(reg(string))