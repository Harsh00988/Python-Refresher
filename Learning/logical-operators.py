# logical operators (and,or,not) - used to check if two or more conditionals statement

# and - both the condition should be true
#or - any 1 condition should be true
#not - unary operator - changes true to false and false to true.

temp = int(input("What is the temperature outside?: "))

if temp>=0 and temp<=30:
    print("the temperature is good today!")
    print("go outside")
else:
    print("the temperature is bad today")
    print("stay inside")
