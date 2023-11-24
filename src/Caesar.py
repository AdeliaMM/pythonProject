def caesar(todo, key, sym):
    if sym.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        dictionary, dictionary_upper = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        dictionary, dictionary_upper = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if sym in dictionary_upper:
        dictionary = dictionary_upper
    if todo == 0:
        new_dict = dictionary[int(key):] + dictionary[0:int(key)]
    else:
        new_dict = dictionary[len(dictionary)-int(key):] + dictionary[0:len(dictionary)-int(key)]
    sym = new_dict[dictionary.find(sym)]
    return sym


def sym_frequency(text):
    frequencies = {}
    for sym in text:
        if sym.isalpha():
            if sym in frequencies:
                frequencies[sym.lower()] += 1
            else:
                frequencies[sym.lower()] = 1
    frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1]))
    frequencies_keys = list(frequencies.keys())
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if frequencies_keys[0] in alphabet:
        for i in range(5):
            for j in range(5):
                if alphabet.find(frequencies_keys[i]) - alphabet.find(frequencies_keys[j]) == -10:
                    key = alphabet.find(frequencies_keys[i]) - 15
                    if alphabet.find(frequencies_keys[i]) - 5 == key:
                        return key
        return 'error'
    else:
        for i in range(5):
            for j in range(5):
                if ord(frequencies_keys[i]) - ord(frequencies_keys[j]) == 15:
                    key = ord(frequencies_keys[i]) - ord('e')
                    if ord(frequencies_keys[j]) - ord('t') == key:
                        return key
        return 'error'
