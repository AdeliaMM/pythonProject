def caesar(todo, key, sym):
    if sym.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if sym in dictionary:
        dict = dictionary
    else:
        dict = dictionary_upper
    if todo == 0:
        new_dict = dict[int(key):] + dict[0:int(key)]
    else:
        new_dict = dict[len(dict)-int(key):] + dict[0:len(dict)-int(key)]
    sym = new_dict[dict.find(sym)]
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
    if frequencies_keys[0] in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        for i in range(5):
            for j in range(5):
                if "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".find(frequencies_keys[i]) - "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".find(frequencies_keys[j]) == -10:
                    key = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".find(frequencies_keys[i]) - 15
                    if "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".find(frequencies_keys[i]) - 5 == key:
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
