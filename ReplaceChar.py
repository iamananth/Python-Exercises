# Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def ReplaceChar(str):
    firstChar = str[0:1]
    n = len(str)
    remString = str[1:n]
    for i in range(0, n):
        Rstr = remString.replace(firstChar, '$')
    return firstChar + Rstr


print(ReplaceChar("ananth"))
