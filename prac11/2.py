numbers = list(map(int,input().split()))
new_numbers = [x for x in numbers if x != 3]
print(new_numbers)