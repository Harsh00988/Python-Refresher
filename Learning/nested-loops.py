#nested loops = the "inner loop" will finish all of it's iterations before
#               finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Eneter a symbol to use")

for _ in range(rows): #use _ instead of index varibales for throwaway variables
    for _ in range(columns):
        print(symbol, end="")
    print()