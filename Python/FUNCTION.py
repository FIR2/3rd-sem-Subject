# n= int(input("enter a number  "))
# for x in range(1,n+1): 
#     print(x*x,end=' ')
# print()    


#create a function
# def functionName(): 
#     n = int(input("enter a number  "))
#     for x in range(1,n+1): 
#      print(x*x,end=' ')
     
# functionName()#call the function
# functionName()




# def f1(): 
#     a = int(input("enter a number "))
#     print("")
#     b = a**2
#     print("Squar4 of ",a,"is",b)

# f1()


# -------------------------ways to define function---------------------
# 1:takes nothing : return nothing

# def add(): 
#     print("Enter two numbers")
#     a=int(input())
#     b=int(input())
#     c=a+b
#     print("Sum is:",c)
# add() #function call


# def Circle(): 
#     pi =3.14
#     r = int(input("Enter the radius of the curcle "))
#     Area = r*r*pi
#     print("Area of the circle is :",Area)
# Circle()



#--------------------Take nothing : return somthin------------------------
# def add(): 
#     print("Enter two numbers ")
#     a=int(input())
#     b=int(input())
#     c=a+b
#     return c
# x =add()
# print(x)   




#------------------take somthing return somthing-----------------------
# def area(r): 
#     pi = 3.14
#     area = r*r*pi
#     return area
# result = area(2)
# print(result)




# def simpleIntrest(p,t,r): 
#     simpIntrest = p*t*r/100
#     return simpIntrest
# # s = simpleIntrest(1,2,50)    
# # print(s)
# s= simpleIntrest(1,4,100)
# print(s)




# # Default arguments
# def sum(a,b,e): 
#     c = a+b+e
#     print("sum is :",c)
# sum(3,5,20)
# sum(10,30) # give error



# def sum(a,b,c=0): 
#  d=a+b+c
#  print("sum is:",d)
# sum(10,20) 
# sum(2,3,4)



# def  add(a,b=0,c): #give an error
#     d= a+b+c
#     print("sum is:",d)
# add(2,3,4)
# add(20,30)   #Give an error  



# def sumation(a=0,b=0,c=0): 
#     d=a+b+c
#     print("sum is:",d)
# sumation(10)    
# sumation(2,3)
# sumation(2,4,5)   

# write a python program to find the leap year 
# def is_leap(year): 
#     if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
#         leap = True
#     else: 
#         leap = False
#     return leap
# year = int(input()) 
# print(is_leap(year))
              
# n = int(input())
# i = 1
# while i <= n: 
#     print(i, end='')
#     i+=1      
    
              
              
# Python program to add two numbers
# n1 =19
# n2 = 20

# sum = n1 + n2
# print("sum of {0} and {1} is {2}" .format(n1,n2,sum))



#         #   OR
# a = input("enter first num ")
# b = input("enter second num ")
# sum = float(a)  + float(b)
# print("sum of {0} and {1} is {2}" .format(a,b,sum))


#         #  OR
# def add(a,b): 
#     return a+b
# num1 = 15
# num2 = 20

# sum_of_Twonumbers = add(num1,num2)

# print("sum of {0} and {1} is {2}". format(num1,num2,sum_of_Twonumbers))




# question : Write a program  to maximum of two numbers
# a = int(input("Enter first number "))
# b = int(input("Enter a second number "))
# def maximum(a,b): 
#     if a >= b: 
#         return a
#     else: 
#         return b   
# result = maximum(a,b)
# # print("Maximum number is:",result) 
# print("Maximum of {0} and {1} is {2}".format(a,b,result))       

  
        # OR
# a  =20
# b= 30
# maximum = max(a,b)
# print(maximum)
        
        #  OR
# def maximum(): 
#     a = 20
#     b = 30
#     maximum = max(a,b)
#     print(maximum)
# maximum()    

        #  OR
        # USE OF TERNARY OPERATOR    
        #  
# a =10
# b = 20

# print("maximum number:",a if a > b else b)


        #   OR
# def fun(a,b): 
#     print("Maximum number is:",a if a > b else b)        
# a =2
# b=-20
# fun(a,b)   
#        










# QUESTION : Python Program for factorial of a number(using recursion)

# number = int(input("Enter a numbers  "))          
# def factorial(n): 
#     # base case
#      if n==0: 
#         return 1
#      if n==1: 
#         return 1 
#      return n*factorial(n-1) 
# result = factorial(number)
# print("factorial of",number,"is:",result)
                 



    

