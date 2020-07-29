"""1. Write a program to find out if a string is a palindrome.
 The string may contain spaces as well as special characters.
 The program should ignore the special characters and determine whether the string is a palindrome or not.
 (For example the string can be “m ad..am”. 
 In this case the string should be read as “madam” which is a palindrome.)
"""
import re # import regular expressions library

x=input("Enter string :")  
formatted_string=re.findall("[a-zA-Z0-9]",x) # using findall we select only the characters we need and add them to a list
print("Formatted String :",end=" ")
print(*formatted_string,sep='')
rev=formatted_string[::-1] # use string slicing to reverse the formatted list
if(rev==formatted_string):
    print("It is a palindrome")  # if both are same
else:
    print("Not a palindrome")
