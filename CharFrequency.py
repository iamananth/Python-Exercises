#checking the character frequency in a string.

def charFreq(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(charFreq("Ananth"))