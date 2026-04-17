lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
start, end = map(int, input().split())

for i in range(end-1, start-1, -1):
    lst2.append(lst1.pop(i))

print(lst1)
print(lst2)
