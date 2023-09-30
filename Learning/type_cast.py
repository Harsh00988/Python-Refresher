#type casting - convert the data type of a value to another data type
#implicit - automatically converts one data type to another
# -- generally python promotes conversion of lower datatype to higher data type to avoid data loss

#explicit - externally specifying which type to convert


x = 1 #int
y = 1.23 #float
# z = x + y float

x = str(x)
y=str(y)
z=x + y

print(z)