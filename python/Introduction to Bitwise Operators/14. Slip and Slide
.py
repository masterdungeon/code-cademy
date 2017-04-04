def flip_bit(number,n):
    mask=(0b1 << n-1)
    desired=number ^ mask
    return bin(desired)
