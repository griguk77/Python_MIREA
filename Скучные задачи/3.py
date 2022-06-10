def main(n, b):
    result = 0
    for c in range(1, n + 1):
        result += (c / 81 - c ** 3 - 16 * c ** 2) ** 2
    for i in range(1, b + 1):
        result += 1 - i - i ** 5
    return result
