def vernam(todo, key, sym):
    if sym.lower() in "abcdefghijklmnopqrstuvwxyz":
        sym = bin(ord(sym))
        for dig in sym[4:]:
            dig = xor(dig, key, key_index) #доделать
