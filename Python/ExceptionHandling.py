# =====-------------Exception Handling------------========

# a = input("Enter a number: ")
# print(f"Multiplication Table of {a} is :")
# try: 
#      for i in range(1,11):
#       print(f"{int(a)}*{i} = {int(a)*i}")
# except: 
#      print("Sorry Invalid Input !")

# print("print some of the code")
# print("End of the program..")    



# #=======-----------Value Error---------=========
# try: 
#   num = int(input("Enter an Enteger: "))
# except ValueError: 
#     print("NUmber enter is not a integer")  



# try: 
#   num = int(input("enter a numbers: "))
#   a =[2,8,3,7]
#   print(a[num])
# except ValueError: 
#   print("number enter is not integer")
# except IndexError: 
#   print("IndexError")  




# -------------use of else in Exception handling--------------------
try:
  def area(): 
    l =input("enter lenght: ")
    b = input("enter breadth: ")
    print(l*b);
  area()  
  
except: 
  print("Somthing want wrong")  
else:
  print("Nothing want wrong") 




#------------- use of finally keyword it is always exicute-----------
# try: 
#   print(x)
# except: 
#   print("Somthing went wrong")
# finally: 
#   print("the 'try except' is finished")  




#88888888888888=============
# def gfg():
#  try: 
 
#    l = [3,5,2,8]
#    i= int(input("Enter the index: "))
#    print(l[i])
#    return 1
#  except:
#   print("some error ocurred..")
#   return 0 
#  finally: 
#    print("I'm alsways exicuted")

# x = gfg()
# print(x)




# ------------ use of raise custome error-------------
# num =int(input("Enter a Number B/W 5 and 9 : "))
# if(num < 5 or num > 9): 
#   raise ValueError("Value should be  b/w 5 and 9..") 







