# LIST
# list = ["name","lastname","firstname"]
# print(list)
# print(list[0])
# list[0] = "firstname"
# print(list)


# TUPLE
# tuple = ("name","lastname","firstname")
# print(tuple)
# print(type(tuple))
# # tuple[0]= "firstname" error bcz tuple unchangable
# x = list(tuple)
# print(x)
# x[0] = "firstname"
# print(x)
# print(type(x))
# print(len(x))



# join two tuple and list separatly
# l1 = ["2","2","#"]
# l2 = ["3","4","5"]
# l3 = l1+l2
# print(l3)


# t1 = ("firoz")
# t2 = ("ansari")
# t3 = t1 + " " + t2
# print(t3)



# x = "Hello  World"
# print(len(x))


# get the first character of the string
# x = "Hello World"
# y = x[0]
# print(y)


# return the string without any whitespace at the begining or the end
# txt = " Hello world "
# print(len(txt))
# print(txt[1:13])
# print(txt[0:14])


# replace  the character H with a j
# txt = "Hello Im firoz Ansari Hello."
# print(txt)
# txt = txt.replace("H","J")
# # print(txt)


# # print in single line
# print("yes") if 5 > 2 else print("no")
# if 39 > 20 : print("this is correct")



# i=0
# while(i < 5): 
#     i=i+1
#     print(i,end=' ')
#     i+=1


# i=0
# while(i<5): 
#     print(i,end='')


# i=0
# while i<5: 
#     if i==3: 
#         print("jai ho ")
#         break
#     print(i)
#     i+=1
# print("shifted to here")    


# i=0
# while(i<5): 
#     if i==2: 
#         continue 
#     else: 
#         print(i,end=' ')
#         i+=1    



# def fact(n): 
#     fact = 1
#     for i in range(1,n+1): 
#         fact = fact*i 
#     return fact
# ans = fact(5)
# print(ans)
# 
# 
# 
# 
# 
# 
def fun(): 
    a= 3
    b = 4
    return a,b
a,b = fun()
print(a,b)            