n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results=[]
    aa=[]
    for numbers in range(len(lists)):
        aa=lists[numbers]
        for j in range(len(aa)):
            results.append(aa[j])
    return results

print flatten(n)