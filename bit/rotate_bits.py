def rotate(x, N):
    # rotate integer to
    return x >> N | x << 64-N

print(hex(rotate(0x12ABCDEF12ABCDEF12ABCDEF12AB, 8)))

print(hex(0x12ABCDEF12ABCDEF12ABCDEF12ABCDEF12ABCDEF12ABCDEF12ABCDEF12ABCDEF))