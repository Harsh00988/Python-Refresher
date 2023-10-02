# **kwargs = parameter that will pack all the arguments into a dictionary   
#            useful so that a function can accept a varying amount of keyword argunments

def hello(**f):
    # print(f"Hello {kwargs['first']} {kwargs['last']}")
    print("Hello", end=" ")
    for value in f.values():
        print(value, end =" ")
    
hello(title = "Mr.", first = "Harsh", middle="Kumar", last = "Goyal")