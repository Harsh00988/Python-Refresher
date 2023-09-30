#while loop - a statement that will execute its block of code,
#             as long as it's condition remains true.

name = ""
while not name: #instead of using len(name) == 0 put not name
    name = input("Enter your name")
    

print(f"Hello {name}") #use f string for printing -> string interpolation

