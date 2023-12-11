index = -1


def vernam(key, sym):
    global index
    index = (index + 1) % len(key)
    if sym in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        if sym == 'ё':
            sym = 'е'
        dictionary = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        sym = f'{dictionary.find(sym):05b}'
        key_sym = f'{dictionary.find(key[index].lower()):05b}'
    else:
        if sym == 'Ё':
            sym = 'Е'
        dictionary = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        sym = f'{dictionary.find(sym):05b}'
        key_sym = f'{dictionary.find(key[index].upper()):05b}'
    print(sym, key_sym)
    for i in range(5):
        sym = sym[:i] + str(int(sym[i] != key_sym[i])) + sym[i + 1:]
    print(sym)
    sym = dictionary[int(sym, 2)]
    return sym
  
