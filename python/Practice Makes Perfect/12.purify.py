def purify(text):
    ii=0
    new=[]
    for i in range(0,len(text)):
        if text[i]%2==0:
            new.append(text[i])
    return new