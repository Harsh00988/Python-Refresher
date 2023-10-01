# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike the positional arguments
#                     Python knows the names of the arguments that our function receives

# Now we will look at positional arguments

def hello(first, middle, last):
    print(f"Hello {first} {middle} {last}")
    
hello("Kumar", "Goyal", "Harsh") #position of the argument matters

hello(middle="Kumar", last="Goyal", first="Harsh") #This is keyword argument and here the position of the argument doesn't matter
