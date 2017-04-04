def censor(text, word):
    n = len(word)
    str1 = []
    str2 = ""
    str1 = text.split(" ")
    for i in range(0, len(str1)):
        if str1[i] == word:
            str2 += (n * "*")
            str2+=" "
        else:
            str2 += (str1[i])
            str2 += " "
    str2=str2[:-1]
    return str2

