# create a array
cars = ["food","volo","BMW"]
print(cars)
print(type(cars))
# x =cars[0]
# print(x)
# or
print(cars[0])

# Modify the array elements
cars[0] = "Safari"
print(cars)

cars[2] = "3663"
print(cars)

# adding array elements
cars.append(2)
print(cars)

print(len(cars))

# looping in array
for x in cars: 
    print(x,end=' ')

print("")
# Removing Array Elements  
cars.pop(1)
print(cars)  

#  or you can also use the remove()method
cars.remove(2)
print(cars)

# copy() method
y =cars.copy()
print(y)

# clear() method
y.clear()
print(y)

demo = ["@","g","dh","hf"]
print(demo)

# reverse() method
demo.reverse()
print(demo)

# insert() method
demo.insert(3,"Firoz Ansari")
print(demo)

demo.insert(4,455)
print(demo)

#index() method ->give the index number of the array value
print(demo.index("dh"))

# sort() method sort the array value itself
new = [2,3,4,5,34,7,4,2,6]
new.sort()
print(new)





