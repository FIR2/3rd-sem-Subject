# Benefits of inheritance are: 

# It represents real-world relationships well.
# It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
# Inheritance offers a simple, understandable model structure. 
# Less development and maintenance expenses result from an inheritance. 


# Python Inheritance Syntax
# Class BaseClass:
#     {Body}
# Class DerivedClass(BaseClass):
#     {Body}



#***********Single Inheritance**********************
# class parent: 
#     name="mr ramu"

#     def work(self): 
#         print("As a SBI clerk")

# class child(parent): 
#     name = "rohan kumar"
#     def study(self): 
#         print("Mca")
#     def work(self) : 
#         print("study krta hun")    

# p = parent()
# # print(p.name)
# # p.work()

# c= child()
# print(c.name)
# c.work()
# c.study()


#******************Multiple Inheritance******************8

# class employee: 
#     company = "Google"
#     eCode = 120
#     def EmpName(self): 
#         print("firoz,rohan,anari,yshdfsyuhghst,has")


# class freelencer: 
#     company = "fiver"
#     level = 0

#     def upgradeLevel(self): 
#         self.level = self.level+1


# class programmer(employee, freelencer): 
#     name = "rohan"
#     def EmpName(self):
#         print("Ali nam,hdghds,yuhsdyuds   ,shdshgsfc")
    


# e = employee()
# # print(e.company)
# # print(e.eCode)
# p = programmer()
# print(p.company)
# print(p.eCode)
# p.upgradeLevel()
# print(p.level)
# p.upgradeLevel()
# print(p.level)
# p.upgradeLevel()
# print(p.level)
# print(p.name)
# e.EmpName()
# p.EmpName()



#**************  Multilevel Inheritance  **********************

# class Department: 
#     department = "Master of computer application "
#     def fun(self): 
#         print("information technology and computer application")
        
# class Teachers(Department): 
#     name = "teacgers"
#     def teachers(self): 
#         print("A to Z")
# class Student(Teachers): 
#     name = "firoz"
#     age = 25 
#     def branch(self): 
#         print("passing years 2023")

# s =Student()
# print(s.department)
# s.fun()

# print(s.name)
# s.teachers()
# print(s.age)
# s.branch()


# # create  object of teacher class
# t =Teachers()
# t.fun()
# print(t.name)





# *************super() method **********************88
# class Department: 
#     department = "Master of computer application "

#     def something(self): 
#         print("information technology and computer application")
        
# class Teachers(Department): 
#     name = "teacgers"
       
#     def something(self): 
#         super().something()
#         print("A to Z")

# class Student(Teachers): 
#     name = "firoz"
#     age = 25 

    
#     def something(self): 
#         super().something()
#         print("passing years 2023")


# s =Student()
# s.something()


  #**************   class Mehtod ********************************************88
# class Employee:
#      company = "HP"
#      salary = 10000
#      location = "india"

#      def changeSalary(self,salary): 
#         self.salary = salary

# e =Employee()
# # print(e.company) 
# print(e.salary)  

# e.changeSalary(2300)
# print(e.salary)

# print(Employee.salary)

 