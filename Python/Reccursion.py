#write a recursive function to print sum of n natural numbers


def sum(n): 
    if n == 1: 
        return 1
    s = n + sum(n-1)
    return s
result = sum(4) 
print("sum is:",result) 


print(" ")
        #  OR

def addition(m): 
    if m == 1: 
        return 1
    return m + addition(m-1)
result1 = addition(4)
print("sum is:",result1)   



# Write a recursive function to calculate  sum of squares of first n natural numbers
def sumSquare(n): 
    if n == 1: 
        return 1
    return n*n + sumSquare(n-1)   
result2 = sumSquare(4)
print("sum of squares:",result2)    