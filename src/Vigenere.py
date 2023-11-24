keys = -1


def vigenere(todo, key, sym):
    if sym.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if sym in dictionary:
        dict = dictionary
    else:
        dict = dictionary_upper
    global keys
    keys = (keys + 1) % len(key)
    key = dictionary.find(key[keys].lower())
    if todo == 0:
        new_dict = dict[key:] + dict[0:key]
    else:
        new_dict = dict[len(dict) - key:] + dict[0:len(dict) - key]
    sym = new_dict[dict.find(sym)]
    return sym
