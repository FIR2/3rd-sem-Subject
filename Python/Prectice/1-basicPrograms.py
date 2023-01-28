# Question: ---------------add two numbers------------------------

# n1 = input("enter a number: ")
# n2 = input("enter a second number: ")
# sum = float(n1) + float(n2)
# print("sum of {0} and {1} is {2}".format(n1,n2,sum))



# by using lambda to sum of two numbers

# if __name__ == "__main__": 
#     n1= 20
#     n2= 39

#  # Adding two numbers
#     add_twonumbers = lambda n1,n2 : n1+n2

#     # printing sum of the numbers
# print("sum of {0} and {1} is {2}".format(n1,n2,add_twonumbers(n1,n2)))



#by using function to sum of two numbers
# def sum(a,b): 
#     return a+b
# a= 30
# b =20    

# add = sum(a,b)
# # initialise the variables 

# print("sum of {0} and {1} is :{2}".format(a,b,add))
# print("sum is: ",add)


# Question:2------------------------- maximum of two number-------------------------
  
    # 1:-->
    #    using function
# def maxNumber(a,b):  
#     if  a > b: 
#         return a
#     else: 
#         return b   
# a = 49
# b = 37
# max = maxNumber(a,b)
# print("maximum numbers is :",max)


# 2:--->
     #  using max()method
# a = 30
# b = 20
# ans = max(a,b)
# print("maximum is :",ans)


# 3:--->
    #  using ternary operator
# a = -39
# b = -7
# print("Maximum of the :",a if a > b else b)


#4:---> 
    # using lambda method
# a = 30
# b = 49
# maximum  = lambda a,b : a if a > b else b
# print(f"{maximum(a,b)} is a maximum number")


#5:--->
     #using list method
# a=2;b=4
# x=[a if a>b else b]
# print("maximum number is:",x)


#6:--->
     #using sort() method
# a = 8
# b = 7
# d = 37
# x = [a,d,b]
# x.sort()
# print(x)
# print(x[-1])     




# Question:3-------------------------factorial of the numbers--------------\

#1---->
# using function recursion
# def fact(n): 
#     return 1 if n == 1 or n == 0 else n*fact(n-1)
# factorial = fact(4)
# print(factorial)  
# T.C = O(N)
# S.C = O(N)   


# 2--->
      # Iterative approach :
# def fatcoral(num): 
#     if num < 0: 
#         return 0
#     elif num == 0 or num == 1: 
#         return 1
#     else: 
#         fact = 1
#         while num > 1: 
#             fact *= num
#             num -= 1
#         return fact
# num = int(input("Enter a integer number: "))
# print("Factrotial of",num,"is =",fatcoral(num))

# T.C= O(N)
# S.C = O(1)
            


# Question 4:
#   Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
#   you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values
#   and print the table.
# NOTE--> PRINT THE FLOOR OF THE CELSIUA VALUES IF THEY ARE NON-NEGATIVE  ELSE PRINT ITS CEIL VALUES 
# USING FORMAULA C=(F-32)*5/9
        #  Sample Input 1:
        #  0 
        #  100 
        #  20

        #   Sample Output 1:
        #   0   -17
        #   20  -6
        #   40  4
        #   60  15
        #   80  26
        #   100 37

# S= int(input())
# E= int(input())
# W= int(input()) 

# while S<=E: 
#     C= ((S-32)*(5/9))  
#     print(S, end=' ')
#     print(int(C))
#     S+=W        
                 

# Question:5->
# -----write a program to print all permutaions of a string ---

# from itertools import permutations
# perms = list(permutations('abcde'))
# for p in perms:
#  s = ''.join(p)
# print(s)

# ------------or---------
# from itertools import permutations
# perms = [''.join(p) for p in permutations('ABC')]
# print(perms)

#-----------or------------

# def toString(list): 
#     return ' '.join(list)

# def permute(b,startI,endI):
#     if startI == endI: 
#         print(toString(b)) 
#     else: 
#         for i in range(startI,endI+1): 
#             b[startI],b[i] = b[i],b[startI]
#             # recursion  
#             permute(b,startI+1,endI)

#             # backtarking
#             b[startI],b[i] = b[i],b[startI] 
  

# #driver code
# str = "ABC"
# # length of String
# n = len(str)
# # convert string to list
# b = list(str)
# # call permute function 
# permute(b,0,n-1)



# Question 6:--> 
#   ------------WRITE a program to rotate array elements clockwise 
# arr = [1,2,3,4,5,6] # after rotaion//[6,1,2,3,4,5]
# n = 5
# # arr = arr[len(arr)-n:len(arr)] + arr[0:len(arr)-n]
# arr = arr[n:len(arr)] + arr[0:len(arr)-1]
# print(arr) #OUTPUT-->[6,1,2,3,4,5]


# Question 7:-->
      #Given an array with number 1 to n find the missing number
 
# arr = [1,2,3,4,6] 
# n = len(arr)
# for i in range(0,n): 
#     if arr[i] != i+1: 
#         print(i+1)
#         break


# Question 8:-->
      # Write a program to find the 10th prime numbers



# Question:9-->
#     Write python function which takes a variable number of arguments.
# def func(*var): 
#     for i in var: 
#         print(i,end=' ')
# func(1)
# func(32,54)
# func(20,1,6)              

# Question:10-->
    #  WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.
# def seqNumber(list): 
#   if len(list) == len(set(list)): 
#     return True
#   else: 
#     return False


# print(seqNumber([2,1,4,5,2,9,6,1]))
# print(seqNumber([4,5,2,9,6,1]))
# print(seqNumber([1,4,5,9]))
# print(seqNumber([1,6,5,8]))
# print(seqNumber([2,1,2,9,6,1]))




