def naive_mul(x, y):
    assert ((0 <= x <= 100) and (0 <= y <= 100))
    r = x
    for i in range(0, y - 1):
        x = x + r
    assert (x == (r * y))
    return x

print(naive_mul(99, 77))