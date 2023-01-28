# What is the class ?
    #  A class is a user-defined blueprint or prototype from which objects are created.
    #  Classes provide a means of bundling data and functionality together. 
    #  Creating a new class creates a new type of object
    
# what is object ?
    #  An Object is an instance of a Class.
    #  An object consists of : 
       #  State: It is represented by the attributes of an object. It also reflects the properties of an object.
       #  Behaviour: It is represented by the methods of an object. It also reflects the response of an object to other objects.
       #  Identity: It gives a unique name to an object and enables one object to interact with other objects.







# class Test: 
#     # define a variable
#     x = 6
#     y = 5
#     # define a function/method
#     def fi(): 
#         print("Hello World")

#     fi()    
# #    create a object of the class
# obj1 = Test() #cretae a object of the class
# print(obj1.x,obj1.y )


# # Note:- Test is the class  reference variable,it is refer 🇹o
#     #    class object



# class Test: 
#     x = 6 #class variabl
#     y = 7 #class variable
#     def fun(): 
#         print("test")
# t1 = Test()
# # Note:- t1 is the reference variable and its refere to to instance 
#     #    object   
      


# #-----======     __init__ function    ======---------
# # class Student: 
# #     # define class variable
# #     x =5
# #     t =3
# #     def __init__(self): 
# #         a = 8 #This is a local variable bcz he is inside function
# # t1 = Student()





# class Student: 
#     # define class variable
#     x =5
#     y =3
#     def __init__(self):
#         self.a = 4
# t1 = Student() # autometically call  __init__(t1)   
# # Note: - when create  object of the class autometically call
# #        __init__ function and pass t1 as a argument implicitly





# class Student: 
#     x = 6
#     y = 8
#     def __init__(self,a): 
#         self.a = a
# t1 = Student(6)  ##  __init__(t1,6)

# # Note:- right side  a and argument wala a is a local variable 
#     #    but left side is a instance object variable




# # create a class
# class Person: 
#     def __init__(self,name,age): 
#         self.name = name
#         self.age = age
# p1 = Person("firoz",26)#object create kr liye          
# print(p1.name,end=':')
# print(p1.age)


# #=============----------   __str__() function -------------====================
# class Person: 
#     def __init__(self,name,age): 
#         self.name = name
#         self.age = age
#     def __str__(self): 
#         return f"{self.name} {self.age}" 
# p1 = Person("firoz",25)
# print(p1)   



# #=======================================

# class rohan: 
#     def __init__(self,name,age): 
#         self.name = name
#         self.age = age
#     def __str__(self): 
#         return f"{self.name}{self.age}" 
# p1 = Person("Rohan",20)
# print(p1)   



# #====  object method-------------
# class teacher: 
#     def __init__(self,name,age): 
#         self.name = name
#         self.age = age

#     def Myname(self): 
#         print("Hi my name is :" + self.name)
# p = teacher("pr us",69)
# p.Myname()  #this is object method          





# 09-pr-01

# class Programmer: 
#     company = "Microsoft"

#     def __init__(self,name,product): 
#          self.name = name
#          self.product = product

#     def info(self): 
#         print(f"the name of the{self.company} programmer is{self.name} and product is{self.product}")
# firoz = Programmer("firoz","jumbo")
# rohan = Programmer("djjs","jsdhjsd") 
# firoz.info()
# rohan.info()



# # 10-pr-02

# class calculater: 
#     def __init__(self,num): 
#         self.num = num

#     def square(self): 
#          print(f"the square of the{self.num} is{self.num **2}")
#     def squareroot(self):
#         print(f"squareroot of the{self.num} is {self.num **0.5}")
#     def quabe(self): 
#         print(f"quabe of the {self.num} is {self.num**3}")
# obj = calculater(9)     
# obj.square()
# obj.squareroot()
# obj.quabe()   



# 11-pr-03

# class sample: 
#     a ="firoz" 
   
# obj =sample()
# obj.a="tannu"
# # sample.a="shgdbsdg"
# print(sample.a)
# print(obj.a)
# # print(obj.a)



# 12-pr-04

# class calculater: 
#     def __init__(self,num): 
#         self.num = num

#     def square(self): 
#          print(f"the square of the{self.num} is{self.num **2}")

#     def squareroot(self):
#         print(f"squareroot of the{self.num} is {self.num **0.5}")
        
#     def quabe(self): 
#         print(f"quabe of the {self.num} is {self.num**3}")

#     @staticmethod
#     def greet(): 
#         print("*****Hello this is calculater using python*****")   

# obj = calculater(9)  
# obj.greet()   
# obj.square()
# obj.squareroot()
# obj.quabe() 



# 13-pr-05
# class Train: 
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare 
#         self.seats=seats

#     def getStaus(self): 
#         print("********************************")
#         print(f"name of the train is {self.name}")
#         print(f"the seats availabe in the tarin are {self.seats}")  
#         print(f"******************************")
    
#     def fareInfo(self): 
#         print(f"the price of the ticket is : Rs {self.fare}")
#         print(f"******************************")

#     def bookTicket(self): 
#         if(self.seats > 0): 
#             print(f"Your ticket has been booked ! your seat no.is {self.seats}")    
#             self.seats = self.seats-1
#         else: 
#             print("sorry this train is full ! kindly try in tatkal ")


# intercity = Train("Intercity Express:14234",90,2)  
# intercity.getStaus()  
# intercity.fareInfo()
# intercity.bookTicket() 
# intercity.bookTicket()  
# intercity.bookTicket()     




# 14-pr-06
class Test: 
    def __init__(add,n1,n2): 
        add.n1 = n1
        add.n2= n2
    def sum(add): 
        print(f"sum of the {add.n1} and {add.n2} is {add.n1+add.n2}")

g=Test(3,5)
g.sum()







        