def reverse(text):
    str1=""
    for i in range(len(text)-1,-1,-1):
        str1+=text[i]
    return str1
        
