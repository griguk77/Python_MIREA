def del_none(list):
    dup_free = []
    for i in range(len(list)):
        if list[i][0] is not None:
            dup_free.append(list[i])
    return dup_free


def count(list):
    for j in range(len(list)):
        str = list[j][0]
        i = 0
        i = str.find(";", i) + 1
        s = ""
        while i < len(str):
            s += str[i]
            i += 1
        s += "00"
        list[j][0] = s
    return list


def name(list):
    j = 0
    for j in range(len(list)):
        str = list[j][2]
        i = 0
        i = str.find(" ", i) + 1
        s = ""
        while i < len(str):
            s += str[i]
            i += 1
        list[j][2] = s
    return list


def date(list):
    for j in range(len(list)):
        str = list[j][0]
        s = ""
        s += str[6]
        s += str[7]
        s += '/'
        s += str[3]
        s += str[4]
        s += '/'
        s += str[0]
        s += str[1]
        list[j][1] = s
    return list


def transform(mat):
    L = []
    for i in range(3):
        L.append(list())
        for j in range(len(mat)):
            L[i].append(mat[j][i])
    return L


def main(list):
    return (transform(name(count(date(del_none(list))))))
