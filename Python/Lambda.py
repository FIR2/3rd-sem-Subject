# def add(a,b): 
#     return a+b 
# s = add(3,4)
# print(s)

# x = add
# #  find id of function object 
# print(id(add))
# # also copy of id in x variable
# print(id(x))


# k = (lambda a,b: a+b)
# print(k(2,4))
# print(k)


# CALCUALTE FACTORIAL OF  A NUMBER USING RECURSIVE LAMBDA EXPRESSION

# k=lambda n : 1 if n==0 or n==1 else n*k(n-1) 
# print(k(4))



# Use that function definition to make a function that always doubles the number you send in:

# def myfun(n): 
#     return lambda a : a*n
# call = myfun(2)    
# print(call(11))


# sum of numbers
# def sum(a,b): 
#     return lambda n: n+a+b
# call = sum(2,8)
# print(call(10))    