number = int(input())
dividers = [x for x in range(1,number+1) if number % x ==0]
print(dividers)