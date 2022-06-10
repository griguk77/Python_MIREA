def main(n):
    if n == 0:
        return 0.98
    else:
        return 4 - ((main(n - 1)) ** 2) / 23 - main(n - 1)
