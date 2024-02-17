# for i in range(1,10):
#     if(i%2==0):
#         print(i)

# for i in "Shubham":
#     print(i)

#pattern using nested loop

r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

for i in range(r):
    for j in range(c):
        print("#",end="")
    print()