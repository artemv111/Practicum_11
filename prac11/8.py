string = input()
def f(string):
    '''
    Функция разбивает слово на символы и сортирует их в алфавитном порядке
    '''
    symbols = []
    for symbol in string:
        symbols.append(symbol)
    symbols.sort()
    return ''.join(symbols)
print(f(string))
