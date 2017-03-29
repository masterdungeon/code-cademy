def remove_duplicates(text):
    new =[]
    for i in range(0,len(text)):
        if text[i] in new:
            continue
        else:
            new.append(text[i])
    return new
        