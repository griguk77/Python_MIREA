print([int(input()), int(input()), int(input())])
print(len(set(input("Введите числа через пробел:").split())))
print([input(), input(), input()][::-1])

s = [9, 1, 5, 3, 6, 6, 4, 3, 7, 9, 5, 4, 6, 2, 1]


def func4(s, x):
    return [i for i in range(len(s)) if s[i] == x]


print(func4(s, 6))


def func5(s):
    return sum([x for i, x in enumerate(s) if i % 2 == 0])


print(func5(s))

print(max([1, 2, 3, 4], [3, 4, 5], key=len))
