def transpouse(mat):
    matrix = []
    for i in range(len(mat[0])):# mat - изначальная матрица
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(mat[j][i])
    return matrix

# Убираем все повторяющиеся строки

def delet(List_t: list):
    List_with_uniq = []
    seen = set()
    for x in List_t:
        hsh = tuple(x)
        if hsh not in seen:
            List_with_uniq.append(x)
            seen.add(hsh)
    return(List_with_uniq)
# Убираем строку с None


def delet_none(List_with_uniq: list):
    t = 0
    stop = len(List_with_uniq)
    i = 0
    while (stop == len(List_with_uniq)):
        for j in range(len(List_with_uniq[0])):
            if (List_with_uniq[i][j] is None):
                t += 1
        if (t == len(List_with_uniq[0])):
            del List_with_uniq[i]
        t = 0
        i += 1
    return(List_with_uniq)


# Форматируем строки
def forma(List_with_uniq: list):
    for i in range(len(List_with_uniq)):
        for j in range(len(List_with_uniq[0])):
            if (List_with_uniq[i][j][1] == '.'):
                List_with_uniq[i][j] = List_with_uniq[i][j]+"000"
            elif (List_with_uniq[i][j][0] == '+'):
                List_with_uniq[i][j] = List_with_uniq[i][j][7:16]
            else:
                List_with_uniq[i][j] = List_with_uniq[i][j].replace('-', '/')
    return(List_with_uniq)


def main(List: list):
    return(forma(delet_none(delet(transpouse(List)))))

A=[[None, "0.7", "21-04-2001", "+7 343 244-10-58", "+7 343 244-10-58"],[None, "0.3", "25-05-2004", "+7 349 056-94-52", "+7 349 056-94-52"],[None, "0.1", "19-12-2001", "+7 244 195-20-57", "+7 244 195-20-57"],[None, "0.2", "18-11-2004", "+7 019 985-40-14", "+7 019 985-40-14"]]
print(main(A))

