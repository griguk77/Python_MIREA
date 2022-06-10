def del_dup(list):
    dup_free = []
    for i in range(len(list)):
        if list[i] not in dup_free:
            dup_free.append(list[i])
    return dup_free


def bol(list):
    for i in range(len(list)):
        if list[i][3] == "true":
            list[i][3] = "Y"
        else:
            list[i][3] = "N"
    return list


def mail(list):
    j = 0
    for j in range(len(list)):
        str = list[j][1]
        i = 0
        i = str.find("@", i) + 1
        email = ""
        while i < len(str):
            email += str[i]
            i += 1
        list[j][2] = email
    return list


def date(list):
    for j in range(len(list)):
        d = ""
        p = ""
        str = list[j][0]
        i = 2
        while str[i] != "&":
            d += str[i]
            i += 1
        list[j][1] = d
        p += str[i + 1]
        p += str[i + 2]
        p += str[i + 3]
        r = p
        p += str[i + 4]
        pp = float(p)
        rr = float(r)
        rr += 0.04
        if pp > rr:
            rr += 0.06
        else:
            rr -= 0.04
        rr = int(rr * 100) / 100
        list[j][0] = "{:.1f}".format(rr)
    return list


def main(list):
    return (date(mail(bol(del_dup(list)))))
