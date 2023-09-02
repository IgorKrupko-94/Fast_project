WORD = 'sherif'

symbols: str = input()

count_symbols = {}
for elem in symbols:
    if elem in count_symbols:
        count_symbols[elem] += 1
    else:
        count_symbols[elem] = 1

if 'f' in count_symbols:
    count_symbols['f'] //= 2

count_symbols_list = []
for symbol in WORD:
    count_symbols_list.append(count_symbols.get(symbol))

if None in count_symbols_list:
    print(0)
else:
    print(min(count_symbols_list))
