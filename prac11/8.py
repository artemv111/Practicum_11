string = input()
def f(string):
    symbols = []
    for symbol in string:
        symbols.append(symbol)
    symbols.sort()
    return ''.join(symbols)
print(f(string))