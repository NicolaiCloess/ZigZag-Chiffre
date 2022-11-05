
def bestimme_reihenfolge(wort):
    wort = wort.lower()
    indizes = []
    indizes_sorted = []
    for c in wort:
        indizes.append(ord(c))
        indizes_sorted.append(ord(c))
    indizes_sorted.sort()

    reihenfolge = []
    for i in range(len(wort)):
        reihenfolge.append(indizes_sorted.index(indizes[i]))

    return reihenfolge

def update_indexlist(indexlist, max_index, step, number):
    indexlist = indexlist

    new_indexlist = []
    if len(indexlist) > 1:
        for i in range(len(indexlist)):
            if indexlist[i] + step <= max_index:
                new_indexlist.append(indexlist[i] + step)
            if indexlist[i] - step >= 0:
                new_indexlist.append(indexlist[i] - step)

            if indexlist[1] * 2 > max_index and indexlist[1] * 2 - step <= max_index:
                new_indexlist.append(indexlist[1] * 2 - step)

    else:

        new_indexlist.append(step)
        if (max_index - step + (number * 2 - 2 - max_index)) <= max_index:
            new_indexlist.append((max_index - step + (number * 2 - 2 - max_index)))


    cleared_indexlist = []
    for i in new_indexlist:
        if i not in cleared_indexlist:
            cleared_indexlist.append(i)

    cleared_indexlist.sort()

    return cleared_indexlist

def verschlüssele(text, zahl, wort=""):
    if len(wort) != zahl and wort != "":
        return("ERROR: Das Wort muss so lang wie die eingegebene Zahl sein")
    elif zahl <= 1:
        return("ERROR: Verschlüsselung muss mindestens aus 2 Zeilen bestehen")
    elif wort == "":
        reihenfolge = [i for i in range(zahl)]
    
    else:
        reihenfolge = bestimme_reihenfolge(wort)
    
    new_text = "".join(text.upper().split())
    if zahl >= len(new_text):
        return "ERROR: Du musst mindestens eine Zeile weniger haben als dein text lang ist"
    encoded = ""
    indexlist = []
    index = 0
    zeilen = {}
    while index < len(new_text):
        indexlist.append(index)
        index += (zahl - 1) * 2

    zeilen[0] = indexlist
    ursprung = indexlist
    for i in range(1, zahl):
        step = i
        indexlist = update_indexlist(ursprung, len(new_text) - 1, step, zahl)
        zeilen[i] = indexlist

    for r in reihenfolge:
        for k in zeilen[r]:
            encoded += new_text[k]

    return encoded


def entschlüssele(text, zahl, wort=""):

    if len(wort) != zahl and wort != "":
        return "ERROR: Das Wort muss so lang wie die eingegebene Zahl sein"
    elif zahl <= 1:
        return "ERROR: Verschlüsselung muss mindestens aus 2 Zeilen bestehen"
    elif wort == "":
        reihenfolge = [i for i in range(zahl)]

    else:
        reihenfolge = bestimme_reihenfolge(wort)

    if zahl >= len(text):
        return "ERROR: Du musst mindestens eine Zeile weniger haben als dein text lang ist"
    indexlist = []
    index = 0
    zeilen = {}
    while index < len(text):
        indexlist.append(index)
        index += (zahl - 1) * 2


    zeilen[0] = indexlist

    ursprung = indexlist

    for i in range(1, zahl):
        step = i

        indexlist = update_indexlist(ursprung, len(text) - 1, step, zahl)
        zeilen[i] = indexlist

    decoded = ""
    index_reihenfolge = []

    test = {}
    for r in reihenfolge:
        for k in zeilen[r]:
            index_reihenfolge.append(k)

    for i in range(len(index_reihenfolge)):
        test[index_reihenfolge[i]] = text[i]

    for r in range(len(text)):
        decoded += test[r]
    return decoded

res = verschlüssele("Dasisteincoolersatzam", 21)
print("VERSCHLÜSSELT:", res)

res2 = entschlüssele("ISEGHEOHFEIIEEMTCTDTEBASNIS", 4, "klar")
print("ENTSCHLÜSSELT:", res2)

#res = verschlüssele("DASISTEINCOOLERSATZAM", 3)
#print("VERSCHLÜSSELT:", res)

#res2 = entschlüssele(res, 3)
#print("ENTSCHLÜSSELT:", res2)

