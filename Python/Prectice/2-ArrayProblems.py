# 1:~~~~~~~~~~~~~~~~~~~~Python Program to find sum of array~~~~~~~~~~~~~~~~~~~~~~~#

# 1:-->approach
# def sumArr(arr): 
#   sum = 0
#   for i in arr: 
#     sum = sum+i 
#   return sum 

# # driver code
# arr = []
# # input value in the array
# arr = [1,3,4,2]
# # size of the array
# n = len(arr)

# sumArr(arr)
# print("Sum of the array elements are = ",sumArr(arr))
# # T.C = O(N)
# # S.C = O(1)



#2:--->approach
# Using the built-in function sum()
# arr = []
# arr = [1,2,3,4,5]

# sumArr = sum(arr)
# print("sum of the array elements are:",sumArr)
# # T.C = O(N)
# # S.C = O(1)


#3:===> approach
     #Using enumerate function 
# arr = [2,3,4,5,6,1];s = 0
# for i,a in enumerate(arr):  
#     s+=a
#     print("sum of the array elemenst are :",s)
#  T.C = O(N)
#  S.C = (1)   


# 2:==-------------FIND THE LARGEST ELEMENT OF THE ARRAY-----------------------

# 1:-->approach

# def largestElem(arr,n): 
#     maxi = arr[0]
#     for i in range(1,n): 
#         if arr[i] > maxi: 
#             maxi = arr[i]
#     return maxi
# #End function body

# arr = [2,54,67,2,5,7,9,34,6,79,3]
# size = len(arr)
# largestElem(arr,size)
# print("Largest element of the array is:",largestElem(arr,size))
# T.C=O(N)
# S.C = O(1)


# 2:-->approach
#using built-in function max()
# def maximumEle(arr,n): 
#     ans = max(arr)  # T.C = O(N)
#     return ans      # S.C = O(1)

# arr = [23,4,2,5,2,6,7,4,2.5,1,5,34]
# n = len(arr)
# Maxi_Elemenet = maximumEle(arr,n)
# print("Maximum element of the array is :",Maxi_Elemenet)


# # Approach 3 (Using sort() function):
# def largestElem(arr,len): 
#      arr.sort()
#      return arr[len-1]

# arr = [3,2,4,3,45,56,2,65,8,34,6,7,4,5,34,65,]
# len = len(arr)
# largestElem(arr,len)
# print("largest element of the array is :",largestElem(arr,len))

# T.C= O(N)
# S.C = O(1)


# def fibonacci(n) : 
#      if n==0: 
#           return 0
#      elif n==1 : 
#           return 1
#      else: 
#           return fibonacci(n-1)+fibonacci(n-2)
# num = int(input("enter a number: "))
# for i in range(num): 
#      print(fibonacci(i))



