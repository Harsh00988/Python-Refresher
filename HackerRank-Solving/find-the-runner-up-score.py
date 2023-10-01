n = int(input())
arr = map(int, input().split())

k = sorted(set(arr))
print(k[-2])
