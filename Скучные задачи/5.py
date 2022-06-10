def main(x, y):
    result = 0
    n = len(x)
    for i in range(n):
        result += ((x[i]) ** 3 + (y[n + 1 - 2 - i // 3]) ** 2 +
                   60 * (x[n + 1 - 2 - i])) ** 6
    result *= 96
    return result
