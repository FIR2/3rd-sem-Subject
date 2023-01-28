 
  num = int(input("enter a numbers: "))

  a =[2,8,3,7]
  print(a[num])
except ValueError: 
  print("number enter is not integer")
except IndexError: 
  print("IndexError")  
