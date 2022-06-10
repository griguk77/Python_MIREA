def del_dup_none(list):
    dup_free = []
    for i in range(len(list)):
        if ((list[i][0] is not None) and (list[i] not in dup_free)):
            dup_free.append(list[i])
    return dup_free


def count(list):
    for j in range(len(list)):
        str = list[j][1]
        s = ""
        if str[2] != "0":
            s += str[2]
        s += str[3]
        s += "%"
        list[j][1] = s
    return list


def name(list):
    j = 0
    for j in range(len(list)):
        str = list[j][0]
        i = 0
        i = str.find(";", i) + 1
        s = ""
        while str[i] != "[":
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
        s += str[8]
        s += str[9]
        list[j][0] = s
    return list


def sort(list):
    list = sorted(list, key=lambda l: l[2])
    return list


def main(list):
    return (sort(date(count(name(del_dup_none(list))))))
