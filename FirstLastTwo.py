#Get a string made of the first 2 and the last 2 chars from a given a string

def FirstLastTwo(str):
    if len(str) < 2:
        return ''
    else:
        return str[0:2] + str[-2:]


print(FirstLastTwo("ananth"))
