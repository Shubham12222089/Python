# import os

# pathe = "C:\\Users\\shubh\\OneDrive\\Desktop"

# if(os.path.exists(pathe)):
#     print("That location exists")
#     if os.path.isfile(pathe):
#         print("It is a file")
#     elif os.path.isdir(pathe):
#         print("It is a directory")
# else:
#     print("Does not exists")

file_path = r"c:\\Users\\shubh\\OneDrive\\Desktop\\python\\bro code\\file detection\\test1.txt"
with open(file_path, "r") as f:
    print(f.read())
