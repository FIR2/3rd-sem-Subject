# print("Hello wporls")
# r=0
# r= r+1
# r =int(input()) #take input  from user and type costing
# area = 3.14*r*r
# print(area)


# <-------String in python-------->


# str1 = "firoz"
# str2 ="ansari"
# print(str1+" "+str2)


# print("Plz enter the area of circle")
# r =int(input()) #take input  from user and type costing
# area = 3.14*r*r
# print("Area is : ",area)
# # print(area)


# If Elif Else | While Loop | 
# print("Enter the a number")
# num = int(input())
# if(num>10):
#     print("Num is greater then 10")
# elif(num<10):
#     print("Num is  less then 10")
# else:
#     print("Equal")    



# use of while loop in python
# print("Enter a number")
# num = int(input())
# while(num>10):
#     print("count of round")
#     num = num-1
#     # break;


# <--------------------Guessing the Number Game-------------------------->
# import random

# rNumber = random.randint(1,10)

# while(True):
#     print("Enter a number")
#     num = int(input())
#     if(num>rNumber):
#         print("Wrong guess, plz try a smallar number")
#     elif(num < rNumber):
#         print("Wrong guess, plZ try a greater number")   
#     else:
#         ("congrats you've guessed number")
#         break;     


# <--------------- For Loop | Functions in Python | Import Statement |--------------->
# for loop

# for x in range(5):
#     print(x)

# for y in range(6):
#     print("0 se lekar kar 5 tk print")

# for z in range(3,10):
#     print(z)


# for  x in range(2,20,2):
#     print(x)


# <--------------Function----------------->
#  def myFun():
#     print("Hi! i'am  Firoz Ansari.")
# myFun()   



# def myFun(a,b):#pass argument a and b
#     print(a+b)

# myFun(3,7) #call function



# return function value
# def sumFun(a,b):
#     return a+b
# result = sumFun(4,6)#call function
# print(result)

# def printhell():
#     print("Hello")  
       
# number = 100


# a = '''Hi Im firoz ansari from khadda'''
# print(a)

# b = """"""Hi Im firoz ansari""""""

# username = input("Enterusername :")
# print("User name is: "+username)

# x = "Department of ITCA"
# Y = "MMMUT Gorakhpur"
# z = x+Y

# print("I am studying in " + " " +"MCA at"+z)


# arithmetics operator
# a= 2
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)
# print()


# # Identity operator
# x= ["a","b"]
# y = ["1","2"]
# z=x
# print(z is not x)
# print(x is not y)
# print(z is not y)
# print(y is not z)
# print(z!=x)
# print()


# # Membership operators
# x= ["apple","banana"]
# print("apple" in x)
# print("banana" not in x)
# print("save" not in x)
# print()

# # if elif condition
# # use of identation
# if 5 > 2:
#     print("5 is greater than 2")

# a = 20
# b = 20
# if a > b:
#     print(" a is greatre than b")
# elif a==b:
#     print("a is equal to b")   
# print()


# x = input("Enter x")
# y = input("Enter y")
# if x > y: 
#     print(" x is greatre than y")
# elif x < y:
#     print(" x is less than y ")
# else:
#     print("x is equal to y")
#     print()
#     print()


 # Casting can be done using constructors : int( ), float( ), str( )
# a = int(20)
# b=int(20.90)
# c = float(3)
# d = str(90)
# print(a)
# print(b)
# print(c)
# print(d)
# print(type(d))

# for loop
# list = ["apple","banana","cherry"]
# for x in list:
#  print(x)
# for x in "banana":
#  print(x)
#  print()

# for y in "apple":  
#  print(y) 

# fruits = ["apple", "banana", "cherry"]
# for x in fruits: 
#   print(x)
#   if x == "banana": 
#     break 

# list = ["firoz","ansari","tonu","ansari","porter"]
# for x in list:  
#     print(x)
#     if x == "ansari": 
#         break


# l = ["1","2","3","4"]
# for x in l:
#   if x == "2":
#     continue
# print(x) 
# 


# for loop with else 
# list = [1,2,3,4,5]
# for x in list: 
#     print(x)
#     x +=1
# else:
#     print("X is no longor")
#     print()


# #  rnage() 
# for x in range(5): 
#     print(x) 
#     print()

#     print()
# for x in range(2,6): 
#     print(x)   

# for x in range(2,30,3):
#     print(x)

# for y in range(1,20,4): 
    # print(y)   

# for z in range(2,10): 
#     print(z)
# else: 
#     print("Finally print all elements") 



# Nseted loop   
# adj = ["red","big","testy"]
# fruits = ["apple","banana","cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)


# for x in range(2,20,3):
#   print(x)



""" -----------------while loop ---------------------"""
# Exapmle:1

# i=1
# while i<6:
#     print(i)
#     i +=1



# Exapmle:2

# i=1
# x = "MCA"
# while i<6:
#     print(x)
#     i = i+1

# using break statment in while loop

# i=1
# while i<5:
#   print(i)
#   if(i == 3):
#     break
#   i=i+1

# Using continue statement in while loop
i =0
while 1 < 6:
 i +=1
 if i==3:
   continue
 print(i)