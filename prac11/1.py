numbers = []
for i in range(10):
    number = int(input())
    numbers.append(number)
new_list = [numbers[i-1] + numbers[i+1] for i in range(1,9)]
print(new_list)