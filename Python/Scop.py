# # local scop
# def myfun(): 
#     x =30 #local scop
#     print(x)
# myfun()    


# # Function Inside Function
# def myfun(): 
#     x =59;
#     def myinnerfun(): 
#         print(x)
#     myinnerfun()
# myfun()        


# # Global Scope
# x =40
# def fun(): 
#     print(x)
# fun()   
# print(x) 

# #Naming Variable
# x = 400
# def myfun(): 
#     x =200
#     print(x)
# myfun()
# print(x)    


# # Global Keyword
# def globalf(): 
#     global x
#     x = 90
#     print(x)
# globalf()
# print(x)    



a = input("Type a two digit number: ")
b = list(a)
print(int(b[0])+int(b[1]))