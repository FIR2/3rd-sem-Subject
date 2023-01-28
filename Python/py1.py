#find the sum of two numbers
# print("Enter two numbers")
# a = 3
# b = 7

# c = a + b

# write a program sum of numbers
# print("Enter a two numbers..")
# a,b = input(),input()

# c =a+b
# print("sum of :",c)

# write a program sum of numbers

# print("Ente two numbers..")
# x,y = int(input()),int(input())

# z = x+y
# print(" sum of the numbers is: ",z )



# if condition
# x = 2
# if x>0: 
#   print("Hello")
#   print("Welcome to space College..")
# print("Bye Bye..")

# write a program to print a given number is positive
# i=int(input("How Many times you want to run the loop  "))
# while i >=1: 
#    a = int(input("Enter a number.."))
#    if a>=0: 
#       print(a, " is positive number.")
#    else: 
#       print(a," is Negative number.")    
#    i=i+1  
# 
# 
# 
# a = int(input("Enter a number "))
# if a>0: 
#     print(a," is positive ")
# if a<0: 
#     print(a," is Negative number ")    


# a = int(input("Enter a number "))
# if a>0: 
#     print(a," is positive ")
# else: 
#     print(a,"is negative number")    


# write a program  to print the grade obtained in a test take marks obtained from user and display the grade
# n = int(input("Enter a number "))
# if 90<n<=100: 
#     print("A")
# elif 80<n<=90: 
#     print("B")
# elif 70<n<=80: 
#     print("C")
# elif 60<n<=70: 
#     print("D")
# elif 50<n<=60: 
#     print("F")
# else: 
#     print("does not exit.")   



# single line if else condition
# Write a program to check  whether a given number is even or odd
# a =int(input("ENTER A NUMBER  "))

# print(a,"is even ") if a%2 == 0 else print(a,"is odd")




# /*---------------------QUESTION---------------------------*/
# write a python script to calculate area of a rectangle 
# l = int(input("Enter the length of the ractangke "))
# w = int(input("Enter the width of the rectangle "))
# # l,w = int(input(" ")),int(input(" "))
# Area = w*l
# print("Area of the Rectangle :",Area)




# /*---------------------QUESTION---------------------------*/
# write a python script to calculate simple intrest
# formula of simple intrest = (p*t*r)/100
# p= principla intrest,r= rate, t= time

# def simple_interest(p,t,r): 
#     i = int(input("How many times you want to run loop  "))
#     while i>0:

#       p = float(input("enter p "))
#       t = float(input("enter t "))
#       r = float(input("enter r "))
#     # print("the principal value is ",p)
#     # print("the time ",t)
#     # print("the rate ",r)
#       si = (p*t*r)/100

#       print("simple interest is ",si)
     
#       i=i-1
# #-------------end loop----------
#     return si
# # --------end finction---------------------------

# # function call
# simple_interest(1,2,3)    




# /*---------------------QUESTION---------------------------*/
# write a program script to remove the last digit from a given number
         # 1st approach
# num = 1235      
# result = num//10
# print(result) 


         #2nd approach
        
# num = 1356
# result=str(num)
# result1 = int((result)[:-1]) #remove digit from end 
# print(result1)

# result2 = int((result)[1:])  # remove digit from start
# print(result2)





# /*---------------------QUESTION---------------------------*/
# n=int(input())
# print("even") if n%2==0 else print("odd")




# a = input("Type a two digit number: ")
# b = list(a)
# print(int(b[0])+int(b[1]))

# n = int(input("Enter the two digit number\n"))
# n = str(n)
# p = int(n[0])+int(n[1])
# print(p)
# n = int(input("enter a numbers: "))
# if n%2== 0: 
#     print("even")
# else: 
#     print("odd")    
num=93
print("even") if num %2 == 0 else print("odd")
    











