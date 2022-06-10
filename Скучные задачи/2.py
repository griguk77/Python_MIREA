def main(y):
    if y < 143:
        return 46 * y + 5 * (y ** 7)
    elif y < 172:
        return 25 * (y ** 3 + y ** 2 + 89) ** 7 + 1 + y ** 3 + 4 * y
    else:
        return 34 + 56 * ((93 + y ** 3) ** 7)
