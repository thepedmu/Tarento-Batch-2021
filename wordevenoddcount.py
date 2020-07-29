
"""
2. Accept a String input
- Print the count of words in the String. Space is assumed to be the separator between words
- Print all numbers that are present in the String and also if they are odd or even. Numbers which are together should be counted as one number.

"""

import re  #import regular expression library

even=list()             # create two lists for even and odd numbers
odd=list()             
x=input("Enter a String : ")
words=len(x.split())    # split the string with space as seperator gives a list of all words
print("Total Words - ",words)
num=re.findall("[0-9]+",x) #findall returns a list of all strings with the pattern [a mumber followed by 1 or more numbers] with greedy find
num=[int(i) for i in num] # cast all numeric strings we got into integers
for i in num:
    if(i%2==0):
        even.append(i)   # add even and odd numbers to corresponding array
    else:
        odd.append(i)
even=set(even)     # remove duplicates
odd=set(odd)
print("Even numbers -",end=" ")
print(*even,sep=',') # print lists with , as seperator
print("Odd numbers -",end=" ")
print(*odd,sep=',')