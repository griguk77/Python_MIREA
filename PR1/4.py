def twelve(x):
    x = x + x
    x = x + x
    x = x + x + x
    return x
a = int (input("Введите число: "))
print(twelve(a))

def sixteen(x):
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    return x
a = int (input("Введите число: "))
print(sixteen(a))

def fifteen(x):
    y = x
    x = x + x
    x = x + x
    x = x + x
    y = y - x
    x = x - y
    return x
a = int (input("Введите число: "))
print(fifteen(a))

def twenty_nine(x):
    y = x
    x = x + x
    x = x + x
    z = x
    x = x + x
    x = x + x
    x = x + x
    x = x + y
    x = x - z
    return x
a = int (input("Введите число: "))
print(twenty_nine(a))
