# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:06:51 2023

@author: Dell
"""

print("Calculator")
print("1.add")
print("2.subtract") 
print("3.Multiply")
print("4.Divide")
#input choice
ch=int(input("Enter Choice(1-4):"))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
    
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)

elif ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")  
1