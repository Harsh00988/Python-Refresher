N = int(input())
a = [] 

for _ in range(N):
    b= list(input().split())
    if b[0] == "insert":
        a.insert(int(b[1]),int(b[2]))
    if b[0] == "print":
        print(a)
    if b[0] == "remove":
        a.remove(int(b[1]))
    if b[0] == "append":
        a.append(int(b[1]))
    if b[0] == "sort":
        a.sort()
    if b[0] == "pop":
        a.pop()
    if b[0] == "reverse":
        a.reverse()