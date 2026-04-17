numbers = list(map(int,input().split()))
chet = [x for x in numbers if x % 2 == 0]
nechet = [x for x in numbers if x % 2 == 1]
print(sum(chet),sum(nechet))