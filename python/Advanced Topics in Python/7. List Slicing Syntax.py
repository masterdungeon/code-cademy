l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[1:10:5]
# [start:end:stride] the first element is start+1 and then gap of stride upto end...