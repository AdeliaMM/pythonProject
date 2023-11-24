keys = -1


def vigenere(todo, key, sym):
    if sym.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        dictionary, dictionary_upper = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        dictionary, dictionary_upper = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if sym in dictionary_upper:
        dictionary = dictionary_upper
    global keys
    keys = (keys + 1) % len(key)
    key = dictionary.lower().find(key[keys].lower())
    if todo == 0:
        new_dict = dictionary[key:] + dictionary[0:key]
    else:
        new_dict = dictionary[len(dictionary) - key:] + dictionary[0:len(dictionary) - key]
    sym = new_dict[dictionary.find(sym)]
    return sym
