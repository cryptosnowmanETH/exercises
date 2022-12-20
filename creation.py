def addup(one: int, two: int) -> int:
    #should be integers 
    sum = one + two 
    return sum

#functions return none by default 
#all functions are variables that do something 

print(addup)

def subtract(x, y):
    return x - y 

print(subtract(2,1))

def calculate(f,number1,number2):
    return f(number1,number2)

#using a function as a parameter 
#must have pure functions: a function that depends on its parameters for all of its inputs, and communicates to outside world via its return statement 

print(calculate(subtract,1,2))

def doit():
    return "abc", 32, [10,11,12]

x = doit()
#returns tuple 
print(x[0])

a,b,c = doit()
#unpacks the tuple into three variables 
print(a)
print(b)
print(c)

xxx = print 
xxx("hello from xxx")

numbers = [1,202,500]
numbers2 = numbers.copy()
#simply copies the name, but does not copy over the values 
#with method copy() it copies over the list to another list instead of just renaming 
numbers2.append("x")
print(numbers)
print(numbers2)

