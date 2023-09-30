#dictionary = A changable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to access a value quickly

capitals = {"India":"New Delhi", 
            "USA":"Washington DC",
            "Australia":"Canberra",
            "Russia":"Moscow"}

# print(capitals["Germany"]) - Will throw an error because germany is not in the list
#print(capitals.get('Germany')) #Much safer way to get a value as it will return none if value does not exist
# print(capitals.keys()) - print keys 
# print(capitals.values()) - print values
# print(capitals.items()) - prints all items
# capitals.update({'Germany' : 'Berlin'}) - updates the dictionary
# capitals.update({'USA' : 'Las Vegas'}) 
# capitals.pop('China') - Remove China
# capitals.clear() - removes everythong in list

for key,value in capitals.items():
    print(key, value)