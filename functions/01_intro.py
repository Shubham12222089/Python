# def hello(a,b):
#     print(a+b)

# hello(4,5)

def evens(n):
    for i in range(n):
        if(i%2==0):
            print(i)

n=int(input("Enter the number : "))
evens(n)