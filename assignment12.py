#1. Write a Python program to Extract Unique values dictionary values?
def unique():
    test_dict = {'gfg': [5, 6, 7, 8],
                'is': [10, 11, 7, 5],
                'best': [6, 12, 10, 8],
                'for': [1, 2, 5]}
    res=list(sorted({ele for val in test_dict.values() for ele in val}))
    return res
print(unique())


#2. Write a Python program to find the sum of all items in a dictionary?
def sum1():
    v={'a': 100, 'b':200, 'c':300}
    k=0
    for i in v.values():
        k=k+i
    return(k)
print(sum1())


#3. Write a Python program to Merging two Dictionaries?
def merge():
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    dict1.update(dict2)
    return dict1
print(merge())


#4. Write a Python program to convert key-values list to flat dictionary?
#from itertools import product
def conv():
    test_dict = {'month': [1, 2, 3],
                 'name': ['Jan', 'Feb', 'March']}
    res=dict(zip(test_dict['month'],test_dict['name']))
    return res
print(conv())


#5. Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict
original_dict =OrderedDict([('a',1),('b',2)])
ins=OrderedDict([('c',3)])
both=OrderedDict(list(ins.items())+list(original_dict.items()))
print (both)


#6. Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict
def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)
    ini_len = 0
    for key, value in dict.items():
        if (key == pattern[ini_len]):
            ini_len = ini_len + 1
        if (ini_len == (len(pattern))):
            return 'true'
    return 'false'
    return(checkOrder(input, pattern))
print(checkOrder('engineers rock','gsr'))


#7. Write a Python program to sort Python Dictionaries by Key or Value?
def dictionairy():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    for i in sorted(key_value.items()):
        print(i, end=" ")
def main():
    dictionairy()
if __name__=='__main__':
    main()