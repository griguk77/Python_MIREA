def del_none(list):
    dup_free = []
    for i in range(len(list)):
        if list[i][0] is not None:
            dup_free.append(list[i])
    return dup_free


def bol(list):
    for i in range(len(list)):
        if list[i][1] == "Y":
            list[i][1] = "1"
        else:
            list[i][1] = "0"
    return list


def name(list):
    j = 0
    for j in range(len(list)):
        str = list[j][2]
        i = 0
        i = str.find(" ", i) + 4
        s = ""
        while i < len(str):
            s += str[i]
            i += 1
        s += ", "
        s += str[0]
        s += "."
        i = 0
        i = str.find(" ", i) + 1
        s += str[i]
        s += "."
        list[j][2] = s
    return list


def date(list):
    for j in range(len(list)):
        str = list[j][0]
        s = ""
        s += str[0]
        s += str[1]
        s += '.'
        s += str[3]
        s += str[4]
        s += '.'
        s += str[8]
        s += str[9]
        list[j][0] = s
    return list


def del_dup(list):
    for j in range(len(list)):
        del list[j][3]
    return list


def main(list):
    return (del_dup(name(bol(date(del_none(list))))))
