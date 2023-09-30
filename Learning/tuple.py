# tuple = collection which is ordered and unchangeable 
#         used to group together related data
#         they are ordered and unchangable

student = ("Harsh", 20, "male") # this is a tuple

#print(student.count("Harsh")) #counts how many times a value has appeared
#print(student.index("male"))  # finds the index of a value 

for x in student:
    print(x)

if "Harsh" in student:
    print("Harsh is here")