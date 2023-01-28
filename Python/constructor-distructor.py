# constructor---
  # Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.
  # Syntax of constructor declaration : 

  # def __init__(self): 
      # body of the constructor


# Types of constructors : 

# default constructor: The default constructor is a simple constructor which doesn’t accept any arguments.
#  Its definition has only one argument which is a reference to the instance being constructed.
# parameterized constructor: constructor with parameters is known as parameterized constructor. 
# The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.      
    


    # Example of default constructor : 
class Collage:
     
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"
 
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
 
 
# creating object of the class
obj = Collage() #__init(obj)__
 
# calling the instance method using the object obj
obj.print_Geek()



    
  #example of parametrised constructor
class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second



# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()


#--------------------------------DISTRUCTOR IN PYTHON---------------------------------#
# Destructors are called when an object gets destroyed.
# The __del__() method is a known as a destructor method in Python. 
# It is called when all references to the object have been deleted
#  i.e when an object is garbage collected. 

# Syntax of destructor declaration : 
 

# def __del__(self):
  # body of destructor


# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj



