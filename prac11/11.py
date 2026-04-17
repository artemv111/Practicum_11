lst = list(map(int, input().split()))
command = input()
direction = command[0]
number = int(command[1:])

if direction == 'R':
    number = number % len(lst)
    if number > 0:
        lst = lst[-number:] + lst[:-number]
else:
    number = number % len(lst)
    if number > 0:
        lst = lst[number:] + lst[:number]

print(lst)