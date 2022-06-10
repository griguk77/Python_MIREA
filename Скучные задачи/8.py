def main(str):
    d = {}
    i = 0
    first = ""
    second = ""
    while ((str.find("var", i)) != -1):
        i = str.find("var", i) + 4
        if (str[i] == " " or str[i] == "#"):
            i += 1
        while (str[i] != " " and str[i] != "="):
            second += str[i]
            i += 1
        i += 2
        if (str[i] == ">"):
            i += 1
        if (str[i] == " "):
            i += 1
        if (str[i] == "\n"):
            i += 1
        while (str[i] != "."):
            first += str[i]
            i += 1
        second = int(second)
        d[first] = second
        first = ""
        second = ""
    return (d)
