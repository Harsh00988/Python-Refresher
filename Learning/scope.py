# scope = the region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global ans locally scoped variable can be created

# Python follws LEGB rule:
#      L = Local
#      E = Enclosing
#      G = Global
#      B = Built-in

name = "Harsh"  # global scope (available inside & outside functions)
def display_name():
    # name = "Goyal"      #local scope (available only inside this function)
    print(name)

print(name)
display_name()