# while True:
#     name = input("Enter your name: ")
#     if(name == ""):
#         break


# for i in range(10):
#     if(i==3 or i == 6 or i==9):
#         continue
#     print(i)

number = "123-456-789"
for i in number:
    if(i=="-"):
        continue
    print(i,end="")