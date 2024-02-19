# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments


def hello(**kwargs):
    print("Hello " + kwargs['first']+" "+kwargs['last'])

hello(first="Shubham",middle="Kumar",last="Jha")