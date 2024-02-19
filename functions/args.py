# *args = parameter that will pack all arguments
# into a tuple useful so that a function can accept a varying
#  of arguments

def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,5,6))

# if we have not used args then we have to pass same number of arguments
# if we passed 4 arguments but fun accepts 3 arguments then it will be an error 
# so args are used
