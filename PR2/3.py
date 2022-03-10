def generate_groups():
    ivbo = []
    for i in range(1, 9):
        ivbo.append('ИВБО-0' + str(i) + '-20')
    ivbo.append('ИВБО-13-20')
    print('ИВБО')
    print(ivbo)
    ikbo = []
    for i in range(1, 10):
        ikbo.append('ИКБО-0' + str(i) + '-20')
    for i in range(10, 28):
        ikbo.append('ИКБО-' + str(i) + '-20')
    ikbo.append('ИКБО-30-20')
    print('ИКБО')
    print(ikbo)
    inbo = []
    for i in range(1, 10):
        inbo.append('ИНБО-0' + str(i) + '-20')
    for i in range(10, 12):
        inbo.append('ИНБО-' + str(i) + '-20')
    inbo.append('ИНБО-13-20')
    inbo.append('ИНБО-15-20')
    print('ИНБО')
    print(inbo)
    imbo = []
    for i in range(1, 3):
        imbo.append('ИМБО-0' + str(i) + '-20')
    print('ИМБО')
    print(imbo)

generate_groups()