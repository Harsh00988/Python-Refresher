# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti"]

food[0] = "sushi" # this is used to update an element

# print(food[0]) #You can use [] for indexing to access a specific element in the list.

# food.append("ice cream") - append an element at the end
# food.remove(food[0]) - remove an item from the list
# food.pop() - removes the last element of the list
# food.insert(position, what to add) - add an elemnt at certain position
# food.sort() - will sort the list - in this case alphabetically
# food.clear() - removes all the elemnts from the list

for x in food:
    print(x)