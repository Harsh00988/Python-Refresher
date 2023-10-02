# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

#print(f"The {animal} jumped over the {item}")
# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item)) #positional arguments
# print("The {animal} jumped over the {item}".format(animal ="cow", item="moon")) #keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = "Harsh"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}, Nice to meet you".format(name))
# print("Hello, my name is {:<10}, Nice to meet you".format(name)) # left align
# print("Hello, my name is {:>10}, Nice to meet you".format(name)) # right align
# print("Hello, my name is {:^10}, Nice to meet you".format(name)) # center align


number = 1000

print("The number pi is {:.2f}".format(number)) # prints upto 2 floating points
print("The number pi is {:,}".format(number)) # add , to all 1000s places
print("The number pi is {:b}".format(number)) # binary value 
print("The number pi is {:o}".format(number)) # ocatal value 
print("The number pi is {:x}".format(number)) # hexadecimal value 
print("The number pi is {:e}".format(number)) # scietific notation 