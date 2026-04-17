string = input()


def otverst(string):
    ch = 0
    symbols = 'abdegopq'
    for symbol in string:
        if symbol in symbols:
            ch += 1
    return ch


def bezotverst(string):
    ch = 0
    symbols = 'abdegopq'
    for symbol in string:
        if symbol.isalpha() and symbol not in symbols:
            ch += 1
    return ch


def two_or_more_holes(string):
    words = string.split()
    new_list = []
    symbols = 'abdegopq'

    for word in words:
        ch = 0
        for i in word:
            if i in symbols:
                ch += 1
        if ch >= 2:
            new_list.append(word)

    return new_list


print(otverst(string), bezotverst(string))
print(two_or_more_holes(string))